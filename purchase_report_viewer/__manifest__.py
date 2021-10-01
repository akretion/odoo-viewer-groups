# Copyright 2018-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Report Viewer',
    'summary': """Access Report submenu to Users and Viewers""",
    'version': '12.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'description': """
Purchase Report Viewer
======================

This module adds access to the menu *Purchase > Reporting* to Purchase Users and Purchase Viewers.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase_viewer'],
    'data': [
        'views/purchase.xml',
    ],
    'installable': True,
}
