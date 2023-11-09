# Copyright (c) 2023, bansi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class BankTransaction(Document):

	def on_load(self):
		self.update_balance()
     
	def on_cancel(self):
		self.update_balance()

	def update_balance(self):
		

		user_account = frappe.get_doc("User Account", self.user_account)
       
		# Get the latest modified transaction
		latest_transaction = max(user_account.bank_transaction, key=lambda t: t.modified) if user_account.bank_transaction else None

		if latest_transaction:
			# Calculate total deposit and withdrawal amounts
			total_deposit = sum([t.amount for t in user_account.transaction_detail if t.transaction_type == 'Deposit'])
			total_withdrawal = sum([t.amount for t in user_account.transaction_detail if t.transaction_type == 'Withdraw'])

			# Update the current balance
			user_account.current_balance = user_account.initial_balance + total_deposit - total_withdrawal
			user_account.save()
			
