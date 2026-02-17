from odoo import _, api, fields, models

class Negocio(models.Model):
    _name = 'repaso_examen.negocio'
    _description = 'Clase negocio'

    nombre = fields.Char(string='Razón Social', required=True)
    cif = fields.Char(string='CIF')