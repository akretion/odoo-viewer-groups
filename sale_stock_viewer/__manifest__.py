# Copyright 2012-2021 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Stock Viewer',
    'summary': """Extends the viewer groups to the 'sale_stock' module""",
    'version': '14.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'description': """
Sale Stock Viewer
=================

This module adds the required read-only Access Control Lists (ACLs) to the group *Sale viewer* when the *sale_stock* module is installed.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['sale_viewer', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'installable': True,
}
