###############################################################################
#
# Copyright(c): 2020 @neo-oien (<https://github.com/neo-oien>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0-standalone.html
# See LICENSE file for full licensing details.
# All Rights Reserved
#
###############################################################################
{
    'name': 'Example module',
    'version': '1.0',
    'summary': 'Short module description',
    'description': '',
    'category': 'Tools',
    'author': '@neo-oien',
    'website': 'https://github.com/neo-oien',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'project'
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # 'templates/',
        'views/example_view.xml',
        'views/menu_items.xml',
        # 'report/',
        # 'data/',
    ],
    'installable': True,
    'application': False,
}
