# Copyright 2012-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Account Viewer',
    'summary': """Adds a group 'Invoice & Payment viewer'""",
    'version': '12.0.1.0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'description': """
Account Viewer
==============

This module adds a group *Invoice & Payment viewer* in the *Accounting & Finance* application. This group grants read-only access to invoices, refunds and payments. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/account.xml',
        'views/product.xml',
    ],
    'installable': False,
}
