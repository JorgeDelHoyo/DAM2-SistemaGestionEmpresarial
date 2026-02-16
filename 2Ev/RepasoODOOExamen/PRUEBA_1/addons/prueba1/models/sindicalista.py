from odoo import _, api, fields, models

class Sindicalista(models.Model):
    _name = 'prueba1.sindicalista'
    _description = 'Representante sindical'

    # Herencia por delegación (Tipo 3)
    _inherits = {'prueba1.trabajador': 'trabajador_id'}

    trabajador_id = fields.Many2one('prueba1.trabajador', string='Trabajadores', ondelete='cascade', required=True)
    seccion_sindical = fields.Char(string='Sección Sindical')
    