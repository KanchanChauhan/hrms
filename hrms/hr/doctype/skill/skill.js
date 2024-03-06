// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Skill', {
	onload: function(frm) {
		frm.set_query("parent_skill", function() {
			return {"filters": [["Skill", "is_group", "=", 1]]};
		});
	},
	refresh: function(frm) {
		// read-only for root skill
		if(!frm.doc.parent_skill && !frm.is_new()) {
			frm.set_read_only();
			frm.set_intro(__("This is a root skill and cannot be edited."));
		}
	},
	validate: function(frm) {
		if(frm.doc.name=="All Skills") {
			frappe.throw(__("You cannot edit root node."));
		}
	}
});
