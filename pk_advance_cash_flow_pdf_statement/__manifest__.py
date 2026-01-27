# -*- coding: utf-8 -*-
{
    'name': "Advance Cash Flow PDF Statement",

    'summary': "Advance Cash Flow PDF Statement | Cash flow account report | custom cash flow report",


    'author': "Irfan Ullah",
    'website': "https://www.youtube.com/@irfanullah",

    'category': 'Uncategorized',
    'version': '18.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/account_wizard_views.xml',
        'report/advance_cash_flow_pdf.xml',
    ],
    'images': ['static/description/banner.png'],
}

