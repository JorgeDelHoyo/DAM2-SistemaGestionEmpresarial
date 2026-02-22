from odoo import _, api, fields, models

class Empresa(models.Model):
    _name = 'examen_empresa.empresa'
    _inherit = 'modulo_base.workplace'
    _description = 'Empresa'
    _rec_name = 'name'

    cif = fields.Char(string='CIF Empresa')
    empleado_ids = fields.One2many('examen_empresa.empleado', 'empresa_id', string='Empleados')
    
    