# Copyright (c) 2023, bansi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UserAccount(Document):
	  
	def on_load(self):
		self.update_balance()

	def update_balance(self):
		
		transactions = frappe.get_list(
			"Bank Transaction",  
			filters={"parent": self.name, "parenttype": "User Account", "parentfield": "transactions_detail"},
			fields=["amount", "transaction_type"],
			order_by="transaction_date DESC",
		)
		
        
		total_balance = self.current_balance
		for transaction in transactions:
			if transaction.transaction_type == "Withdrawal":
				total_balance += transaction.amount
			elif transaction.transaction_type == "Deposit":
				total_balance -= transaction.amount


		self.current_balance = total_balance
		self.save()

		frappe.msgprint(f"Balance updated. New balance: {total_balance}")