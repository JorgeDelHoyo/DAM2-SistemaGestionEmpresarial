from odoo import _, api, fields, models

# 1. Clase Padre
class Negocio(models.Model):
    _name = 'prueba1.negocio'
    _description = 'Clase Negocio General'
    
    name = fields.Char(string='Razón Social', required=True)
    cif = fields.Char(string='CIF')

# 2. Clase Hija (Empresa)
class Empresa(models.Model):
    _name = 'prueba1.empresa'
    _inherit = 'prueba1.negocio' # Hereda nombre y CIF
    _description = 'Empresa específica'

    sector = fields.Char(string='Sector')

    alumno_ids = fields.One2many('prueba1.alumno', 'empresa_id', string='Alumnos en prácticas')
    