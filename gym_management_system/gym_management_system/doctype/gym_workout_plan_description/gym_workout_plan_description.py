# Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymWorkoutPlanDescription(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"gymplan/{self.name}"
