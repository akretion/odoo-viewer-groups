# Copyright 2013-2019 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Project Viewer',
    'summary': """Adds a group 'Project Viewer'""",
    'version': '12.0.1.0.0',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'description': """
Project Viewer
==============

This module adds a group *Project Viewer* in the *Project* application. This group grants read-only access to the Project management. If you add a user to this new group, he should also be in the group *Human Ressources - Employee*.

This module has been written by Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['project'],
    'data': [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'views/project.xml',
    ],
    'installable': True,
}
