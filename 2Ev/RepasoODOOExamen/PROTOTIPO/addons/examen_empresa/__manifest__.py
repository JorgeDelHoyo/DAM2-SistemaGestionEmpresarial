{
    'name': "examen_empresa",

    'summary': "Gestión de Empresas y Empleados",

    'description': """
    Gestión para una empresa heredada del módulo base
    """,

    'author': "Jorge del Hoyo Ballestín",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'modulo_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/empresa_report.xml',
        'views/empresa_views.xml',
        'views/empleado_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True
}

