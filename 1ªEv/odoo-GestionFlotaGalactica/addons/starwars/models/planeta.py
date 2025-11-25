from odoo import _, api, fields, models

class Planeta(models.Model):
    _name = 'starwars.planeta'
    _description = 'Planetas'

    name = fields.Char(string="Nombre del planeta")
    climate = fields.Selection([
        ('arido', 'Arido'),
        ('templado', 'Templado'),
        ('tropical', 'Tropical'),
        ('helado', 'Helado')
    ], string='Clima del planeta')
    