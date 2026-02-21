{
    'name': "modulo_base",

    'summary': "Modulo base proporcionado por el profesor",

    'description': """
    Este es un módulo "PADRE" para proporcionar una herencia simple y múltiple en el examen,
    así mismo va a heredar a una empresa y a un hospital
    """,

    'author': "Jorge del Hoyo Ballestín",
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
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application': True
}

