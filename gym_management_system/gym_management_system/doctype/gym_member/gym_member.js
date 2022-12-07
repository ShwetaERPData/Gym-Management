// Copyright (c) 2022, shweta.chougule@erpdata.in and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	refresh: function(frm) {
		   frm.add_custom_button(
			   "Select Wokout Plan",
			   () => {
				   frappe.new_doc("Book Membership Plans",{
					   booked_by:frm.doc.name,
				    })
			   },
			   "Actions"
		   );
		   frm.add_custom_button(
			   "Book Locker",
			   () => {
				frappe.new_doc("Book Locker",{
					booked_by:frm.doc.name,
				})
			   },
			   "Actions"
		   );
		   frm.add_custom_button(
			   "Book Gym Trainer",
			   () => {
				frappe.new_doc("Book Locker",{
					booked_by:frm.doc.name,
				})
			   },
			   "Actions"
		   );
		   let me = this;
		const months = moment.months();
		const curMonth = moment().format("MMMM");
		months.splice(months.indexOf(curMonth) + 1);
			frm.add_custom_button(
				"Mark Evalution",
				() =>{
				let dialog = new frappe.ui.Dialog(
					{
						title:"Mark Evalution",
						fields:[
							{
								label: __("Member"),
								fieldtype: "Link",
								fieldname: "member",
								options: "Gym Member",
								reqd: 1,
								default: frm.doc.name
							},
							{
								label: __("For Month"),
								fieldtype: "Select",
								fieldname: "month",
								options: months,
								reqd: 1,
								default: curMonth
							},
							{
								"fieldname":"weight",
								"label": __("Weight"),
								"fieldtype": "Data",
								"reqd": 1
							},
							{
								"fieldname":"calories",
								"label": __("calories"),
								"fieldtype": "Data",
								"reqd": 1
							},
							{
								"fieldname":"is_improvement",
								"label": __("Is Improvement"),
								"fieldtype": "Check",
								"reqd": 1
							},
							
							
						],
						primary_action(data) {
							debugger
							    frappe.confirm(__('Would you like to confirm the weight of {0}kg for {1} in the month of select Month{2}?', [data.weight,data.member, data.month]), () => {
									frappe.call({
										
										method: "gym_management_system.gym_management_system.doctype.gym_member_evaltation.gym_member_evaltation.mark_gym_evtuation",
										args: {
										
											data: data
										},
										callback: function (r) {
											if (r.message === 1) {
												frappe.show_alert({
													message: __("Attendance Marked"),
													indicator: 'blue'
												});
												cur_dialog.hide();
											}
										}
									});
								});
							
							dialog.hide();
							list_view.refresh();
						},
						primary_action_label: __('Mark Evaluation')
					}
				)
				dialog.show();
				},
				"Evalution"
			);	
	}
});

