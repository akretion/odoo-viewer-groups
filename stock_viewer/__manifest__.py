# -*- coding: utf-8 -*-
# © 2012-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Viewer',
    'summary': """Adds a group 'Stock viewer'""",
    'version': '10.0.1.0.0',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'description': """
Stock Viewer
============

This module adds a group *Stock viewer* in the *Warehouse* application. This group grants read-only access to the Warehouse management. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['stock'],
    'data': [
        'security/stock_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
