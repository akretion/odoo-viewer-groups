# Copyright 2018-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Report Viewer',
    'summary': """Access Report submenu to Viewers""",
    'version': '12.0.1.0.1',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'description': """
Account Report Viewer
=====================

This module adds access to the menu *Invoicing > Reporting > Management > Invoices* to Invoice Viewers.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account_viewer'],
    'data': [
        'views/account.xml',
        'security/account_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
