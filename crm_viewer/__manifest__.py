# Copyright 2024 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'CRM Viewer',
    'summary': """Extend 'Sale viewer' to CRM""",
    'version': '16.0.1.0.0',
    'category': 'Sales/CRM',
    'license': 'AGPL-3',
    'description': """
CRM Viewer
==========

This is a glue module between the *sale_viewer* and *sale_crm* modules.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'https://github.com/akretion/odoo-viewer-groups',
    'depends': ['sale_crm', 'sale_viewer'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'auto_install': True,
}
