# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import unittest

import frappe


class TestSkill(unittest.TestCase):
	def test_remove_skillt_data(self):
		doc = create_skill("Test Skill")
		frappe.delete_doc("Skill", doc.name)


def create_skill(skill_name, parent_skill=None):
	doc = frappe.get_doc(
		{
			"doctype": "Skill",
			"is_group": 0,
			"parent_skill": parent_skill,
			"skill_name": skill_name
		}
	).insert()

	return doc


test_records = frappe.get_test_records("Skill")