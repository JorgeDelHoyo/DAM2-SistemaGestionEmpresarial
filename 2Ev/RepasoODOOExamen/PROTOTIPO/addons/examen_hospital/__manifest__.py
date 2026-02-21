{
    'name': "examen_hospital",

    'summary': "Gestión de Hospitales y Pacientes",

    'description': """
    Modulo que hereda del base para un hospital
    """,

    'author': "Jorge del Hoyo Ballestín",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','modulo_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hospital_views.xml',
        'views/paciente_views.xml',
        'reports/hospital_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}

