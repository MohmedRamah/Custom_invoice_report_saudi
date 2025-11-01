# -*- coding: utf-8 -*-
{
    'name': "Custom Report",

    'summary': "Using To Can Change  invoice Report shap ",

    'description': """
Using To Can Change  invoice Report shap 
For Any Question Call Us on This Number :
        +966549105226     => Saudi Number
        +201146360623     => Egyption Number
    """,

    'author': "Eng:Muhammad Ramah && Eng:Muhammad El-Nayed ",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/custom_invoice_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

