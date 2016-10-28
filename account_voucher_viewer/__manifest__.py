# -*- coding: utf-8 -*-
# © 2012-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Voucher Viewer',
    'summary': """Extends the group 'Invoice & Payment viewer' to Vouchers""",
    'version': '10.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'description': """
Account Voucher Viewer
======================

This module adds the read-only Access Control Lists (ACLs) on the object account.voucher to the group *Invoice & Payment viewer*.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account_voucher', 'account_viewer'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'installable': True,
}
