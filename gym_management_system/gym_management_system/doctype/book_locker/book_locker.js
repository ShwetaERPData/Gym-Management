// Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Locker', {
	 refresh: function(frm) {
		frm.fields_dict['available_lockers'].get_query = function(doc) {
			return {
				filters: {
					"is_available": '1'
				}
			}
		}
	}
});
