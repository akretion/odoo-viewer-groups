# Copyright 2018-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Report Viewer',
    'summary': """Access Report submenu to Users and Viewers""",
    'version': '12.0.1.0.0',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'description': """
Stock Report Viewer
===================

This module adds access to the menu *Inventory > Reporting* to Stock Users and Stock Viewers.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['stock_viewer'],
    'data': [
        'views/stock.xml',
    ],
    'installable': True,
}
