# Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMember(Document):
	def on_update(self):
		self.create_user()

	def create_user(self):
		frappe.get_doc({
			"doctype":"User",
			"email":self.email,
			"first_name":self.first_name,
		}).insert(ignore_permissions=True)
