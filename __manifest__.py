# -*- coding: utf-8 -*-
{
    'name': "IM Citas",

    'summary': """
        im_citas""",

    'description': """
        Módulo para la gestión de citas de I&M Asesores
    """,

    'author': "CJI Software",
    'website': "https://www.ieselcaminas.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/informeTipos.xml',
        'reports/informeCalculadora.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
