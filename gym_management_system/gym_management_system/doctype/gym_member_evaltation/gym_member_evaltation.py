# Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.query_builder import Criterion
from frappe.utils import cint, cstr, formatdate, get_datetime, get_link_to_form, getdate, nowdate



class GymMemberEvaltation(Document):
	pass

@frappe.whitelist()
def mark_gym_evtuation(data):
	import json
	data = json.loads(data)
	
	evalution = frappe.get_doc(
		{
			"doctype":"Gym Member Evaltation",
			"member":data['member'],
			"month":data['month'],
			"weight": data['weight'],
			"calories":data['calories'],
		    "is_improvement": data['is_improvement'],
		}
	)
	evalution.insert()
	evalution.submit()
	frappe.msgprint("Evalution Saved!!")
	#	attendance = frappe.get_doc(doc_dict).insert()
	#	attendance.submit()
