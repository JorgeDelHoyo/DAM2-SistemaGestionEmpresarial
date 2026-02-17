from odoo import _, api, fields, models

class Trabajador(models.Model):
    _name = 'repaso_examen.trabajador'
    _inherit = 'repaso_examen.persona'
    _description = 'Clase Trabajador hereda de persona'

    puesto = fields.Char(string='Puesto Trabajo')