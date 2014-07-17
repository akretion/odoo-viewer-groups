# -*- encoding: utf-8 -*-
##############################################################################
#
#    Account voucher viewer module for OpenERP
#    Copyright (C) 2012-2014 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Account Voucher Viewer',
    'summary': """Extends the group 'Invoice & Payment viewer' to Vouchers""",
    'version': '1.0',
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
    'active': False,
}
