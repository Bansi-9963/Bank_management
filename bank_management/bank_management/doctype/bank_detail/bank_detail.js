// Copyright (c) 2023, bansi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bank Detail", {
	refresh(frm) {
        frm.add_custom_button('Create Branch', () => {
            frappe.new_doc('Branch Details', {
                bank: frm.doc.name
            })
        })

	},
});
