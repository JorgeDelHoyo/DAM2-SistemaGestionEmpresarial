from odoo import _, api, fields, models

class Recinto(models.Model):
    _name = 'prueba4.recinto'
    _description = 'Recinto'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    capacidad_maxima = fields.Integer(string='Capacidad Máxima', default=100)