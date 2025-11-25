from odoo import _, api, fields, models

class TipoNave(models.Model):
    _name = 'starwars.tipo.nave'
    _description = 'Tipo de la nave'

    name = fields.Char(string="Modelo de la nave")
    fuerza_fuego = fields.Integer(string="Puntos de ataque")
    es_hipervelocidad = fields.Boolean(string="Tiene salto al hiperespacio")
    