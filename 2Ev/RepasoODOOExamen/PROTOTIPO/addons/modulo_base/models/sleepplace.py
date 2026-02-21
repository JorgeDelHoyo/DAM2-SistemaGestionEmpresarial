from odoo import _, api, fields, models

class SleepPlace(models.Model):
    _name = 'modulo_base.sleepplace'
    _description = 'SleepPlace'
    
    cantidad = fields.Integer(string='Cantidad de camas')
    tiene_comedor = fields.Boolean(string='¿tiene comedor?')
    fecha_entrada = fields.Date(string='Fecha entrada')
    fecha_salida = fields.Date(string='Fecha salida')