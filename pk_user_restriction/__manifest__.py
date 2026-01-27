# Irfan Ullah Odoo Technical developer with hands-on experience
# contact Whatsapp: +923349693796 Email: irfanbcs797@gmail.com
# YouTube: https://www.youtube.com/@irfanullah
# -*- coding: utf-8 -*-
{
    'name': "User Restriction  ",

    'summary': """
       Restrict User to  Create, Update, Delete  records""",

    'description': """
       Specific groups for creating, updating, and deleting records, once assign to user then user can't do that operation.
    """,

    # 'price': '2.00',
    # 'currency': 'USD',
    'license': 'LGPL-3',
    'author': 'Irfan Ullah',
    'website': 'https://www.youtube.com/@irfanullah',

    'category': 'Uncategorized',
    'version': '17.0.0.1',
    'depends': ['base'],

    # always loaded
    'data': [
        'security/user_groups.xml',
    ],
    'images': ['static/description/banner.png'],

}
