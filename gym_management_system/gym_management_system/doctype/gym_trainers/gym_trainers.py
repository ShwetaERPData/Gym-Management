# Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymTrainers(Document):
	def on_update(self):
		self.create_user()

	def create_user(self):
		frappe.get_doc({
			"doctype":"User",
			"email":self.email,
			"first_name":self.first_name,
			"last_name":self.last_name,
			"full_name":self.full_name,
			"birth_date":self.dob,
			"mobile_no":self.phone,
			"role_profile_name":"Gym Trainer",
			"module_profile":"Gym Member Profile",
		}).insert(ignore_permissions=True)

	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'
