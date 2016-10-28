# -*- coding: utf-8 -*-
# © 2012-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale MRP Viewer',
    'summary': """Extends the group 'MRP viewer' to the 'sale_mrp' module""",
    'version': '10.0.1.0.0',
    'category': 'Manufacturing',
    'license': 'AGPL-3',
    'description': """
Sale MRP Viewer
===============

This module adds the required read-only Access Control Lists (ACLs) to the group *MRP viewer* when the *sale_mrp* module is installed.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['sale_mrp', 'mrp_viewer', 'sale_viewer'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'installable': True,
}
