frappe.treeview_settings["Skill"] = {
	ignore_fields:["parent_skill"],
	get_tree_nodes: 'hrms.hr.doctype.skill.skill.get_children',
	add_tree_node: 'hrms.hr.doctype.skill.skill.add_node',
	breadcrumb: "HR",
	root_label: "All Skills",
	get_tree_root: true,
	menu_items: [
		{
			label: __("New Skill"),
			action: function() {
				frappe.new_doc("Skill", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Skill") !== -1'
		}
	],
	onload: function(treeview) {
		treeview.make_tree();
	}
};