# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe
from frappe.utils.nestedset import NestedSet, get_root_of

from erpnext.utilities.transaction_base import delete_events


class Skill(NestedSet):

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		skill_name: DF.Data
		disabled: DF.Check
		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Data | None
		parent_skill: DF.Link | None
		rgt: DF.Int

	nsm_parent_field = "parent_skill"

	def autoname(self):
		self.name = self.skill_name

	def validate(self):
		if not self.parent_skill:
			root = get_root_of("Skill")
			if root:
				self.parent_skill = root


	def on_update(self):
		if not (frappe.local.flags.ignore_update_nsm or frappe.flags.in_setup_wizard):
			super(Skill, self).on_update()

	def on_trash(self):
		super(Skill, self).on_trash()
		delete_events(self.doctype, self.name)


def on_doctype_update():
	frappe.db.add_index("Skill", ["lft", "rgt"])


@frappe.whitelist()
def get_children(doctype, parent=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = frappe.json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = {}

	filters["parent_skill"] = parent

	if frappe.db.has_column(doctype, "disabled") and not include_disabled:
		filters["disabled"] = False

	return frappe.get_all("Skill", fields=fields, filters=filters, order_by="name")


@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args

	args = frappe.form_dict
	args = make_tree_args(**args)
	frappe.get_doc(args).insert()