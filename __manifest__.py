# -*- coding: utf-8 -*-
{
    'name': "modulo_coches",

    'summary': """
        modulo para gestionar coches""",

    'description': """
        gestiona de forma comoda los vehiculos de la empresa
    """,

    'author': "pablo andreu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner_menuitemadd_view.xml',
        'views/res_users_Additional_Info_vies.xml',
        'views/res_partner_socialnetwork_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
