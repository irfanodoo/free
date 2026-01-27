# -*- coding: utf-8 -*-
{
    'name': "Sale Quotation Report",

    'summary': """
        Quotation custom report  """,


    'author': " Irfan Ullah",
    'website': 'https://www.youtube.com/@irfanullah',

    'category': 'Uncategorized',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'report/report_tem.xml',
    ],

    'images': ['static/description/banner.png'],
}
