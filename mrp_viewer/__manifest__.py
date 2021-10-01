# Copyright 2012-2021 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'MRP Viewer',
    'summary': """Adds a group 'Manufacturing viewer'""",
    'version': '14.0.1.0.0',
    'category': 'Manufacturing',
    'license': 'AGPL-3',
    'description': """
MRP Viewer
==========

This module adds a group *Manufacturing viewer* to the *Manufacturing* application. This group grants read-only access to the Manufacturing management. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['mrp'],
    'data': [
        'security/mrp_security.xml',
        'security/ir.model.access.csv',
        'views/mrp.xml',
    ],
    'installable': True,
}
