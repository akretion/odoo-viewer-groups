# -*- encoding: utf-8 -*-
##############################################################################
#
#    Purchase viewer module for OpenERP
#    Copyright (C) 2012 Akretion (http://www.akretion.com). All Rights Reserved
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
    'name': 'Purchase viewer',
    'version': '1.0',
    'category': 'Purchase Management',
    'license': 'AGPL-3',
    'description': """This module adds a group 'Purchase viewer' which grants read-only access to the Purchase Management. If you add a user to this new group, he should also be in the group 'Human Ressources - Employee'.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase'],
    'init_xml': [],
    'update_xml': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
