from odoo import _, api, fields, models

class Departamento(models.Model):
    _name = 'academia.departamento'
    _description = 'Departamento'

    name = fields.Char(string="Nombre del departamento")

    # Un departamento contiene varios profesores
    profesor_ids = fields.One2many('academia.profesor', 'departamento_id', string='Profesores Asignados')