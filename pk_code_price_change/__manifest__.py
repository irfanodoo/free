# -*- coding: utf-8 -*-
{
    'name': "All Products price's change",
    'summary': "All Products prices change of same code when we change the price of one code",
    'author': "Irfan Ullah",
    'website': 'https://www.youtube.com/@irfanullah',
    'category': 'Uncategorized',
    'version': '16.0.0.0',
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_varient.xml',
        'views/price_code.xml',
    ],
    'images': ['static/description/banner.png'],
}

