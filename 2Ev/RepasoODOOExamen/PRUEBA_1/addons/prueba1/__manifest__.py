{
    'name': "prueba1",

    'summary': "Prueba 1 para repasar herencia etc",

    'description': """
        Probamos módulos básicos
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
        'views/persona_kanban.xml',
        'reports/informe_empresa.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
}

