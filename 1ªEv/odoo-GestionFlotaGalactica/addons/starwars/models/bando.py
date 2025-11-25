from odoo import _, api, fields, models

class Bando(models.Model):
    _name = 'starwars.bando'
    _description = 'Bando de la flota'
    
    name = fields.Char(string="Nombre del bando", required=True)
    description = fields.Text(string="Descripcion corta")