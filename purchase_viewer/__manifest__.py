# Copyright 2012-2021 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Viewer',
    'summary': """Adds a group 'Purchase viewer'""",
    'version': '14.0.1.0.0',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'description': """
Purchase Viewer
===============

This module adds a group *Purchase viewer* in the *Purchases* application. This group grants read-only access to the Purchase Management. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase'],
    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'views/purchase.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
}
