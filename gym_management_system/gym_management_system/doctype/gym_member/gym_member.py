# Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMember(Document):
	def on_update(self):
		self.create_user()
		self.create_user_permission()

	def create_user(self):
		frappe.get_doc({
			"doctype":"User",
			"email":self.email,
			"first_name":self.first_name,
			"last_name":self.last_name,
			"full_name":self.full_name,
			"birth_date":self.dob,
			"mobile_no":self.phone,
			"role_profile_name":"Gym member",
			"module_profile":"Gym Member Profile",
		}).insert(ignore_permissions=True)
		
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'

	def create_user_permission(self):
		frappe.get_doc({
			"doctype":"User Permission",
			"user":self.email,
			"allow":"Gym Member",
			"for_value":self.first_name +" "+self.last_name+"-"+self.phone,
			"apply_to_all_doctypes":1,
		}).insert(ignore_permissions=True)

	
