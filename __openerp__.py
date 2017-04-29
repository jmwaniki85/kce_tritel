# -*- coding: utf-8 -*-
{
    'name': "tritel",

    'summary': """
        Tritel Extensions to Standard Odoo Modules""",

    'description': """
        This module contains Tritel Extensions to Modules that come with Odoo Off the Box
    """,

    'author': "Tritel Technologies",
    'website': "http://www.tritel.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'General',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/res_partner.xml',
        'views/dimensions.xml',
        #'views/account_voucher.xml'
        'reports/reports.xml',
        'views/res_approvals.xml',
        'views/account_invoice.xml',
        'reports/account_invoice_statements.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
