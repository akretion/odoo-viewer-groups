# Copyright 2012-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Viewer',
    'summary': """Adds a group 'Sale viewer'""",
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'description': """
Sale Viewer
===========

This module adds a group *Sale viewer* in the *Sales* application. This group grants read-only access to Sales Management. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['sale'],
    'data': [
        'security/sale_security.xml',
        'security/ir.model.access.csv',
        'views/sale.xml',
        'views/product.xml',
        'views/partner.xml',
    ],
    'installable': True,
}
