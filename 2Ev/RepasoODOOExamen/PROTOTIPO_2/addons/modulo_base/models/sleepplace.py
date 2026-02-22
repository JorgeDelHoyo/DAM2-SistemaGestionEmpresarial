from odoo import _, api, fields, models

class SleepPlace(models.Model):
    _name = 'modulo_base.sleepplace'
    _description = 'SleepPlace'

    cantidad_camas = fields.Integer(string='Cantidad de camas')
    