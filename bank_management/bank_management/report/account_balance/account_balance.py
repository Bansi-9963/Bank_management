import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        _("Username") + ":Link/User:120",
        _("Branch") + ":Link/Branch Details:120",
		_("Account number") + ":Int:120",

        _("Current Balance") + ":Currency:120"
    ]

def get_data(filters):
    condition = f"`tabUser Account`.current_balance > 140000"
    
    if filters.get("branch"):
        condition += f" AND `tabUser Account`.branch = '{filters['branch']}'"

    return frappe.db.sql(f"""
        SELECT 
            username,
            branch,
			account_number,
			
            current_balance
        FROM 
            `tabUser Account`
        WHERE 
            {condition}
    """, as_dict=1)
