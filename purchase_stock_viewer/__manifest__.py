# Copyright 2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Stock Viewer',
    'summary': """Adds a group 'Purchase viewer'""",
    'version': '12.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'description': """
Purchase Stock Viewer
=====================

This is a glue module between the *puchase_viewer* and *purchase_stock* modules.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase_stock', 'purchase_viewer'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
}
