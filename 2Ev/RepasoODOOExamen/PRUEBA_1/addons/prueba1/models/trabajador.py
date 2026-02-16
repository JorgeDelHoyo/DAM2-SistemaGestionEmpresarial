from odoo import _, api, fields, models

class Trabajador(models.Model):
    _name = 'prueba1.trabajador'
    _inherit = 'prueba1.persona' # Hereda de persona
    _description = 'Trabajador'

    puesto = fields.Char(string='Puesto de Trabajo')
    