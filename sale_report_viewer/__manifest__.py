# Copyright 2018-2021 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Report Viewer',
    'summary': """Access Report submenu to Users and viewers""",
    'version': '14.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'description': """
Sale Report Viewer
==================

This module adds access to the menu *Sales > Reporting* to Sale Users and Sale Viewers.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['sale_viewer'],
    'data': [
        'views/sale.xml',
        'views/product.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
