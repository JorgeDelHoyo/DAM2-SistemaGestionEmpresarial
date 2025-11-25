from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Rango(models.Model):
    _name = 'starwars.rango'
    _description = 'Rango del personal'

    name = fields.Char(string="Titulo")
    nivel_acceso = fields.Integer(string="Nivel del 1 al 10")

    @api.constrains('nivel_acceso')
    def _constrains_fieldname(self):
        for r in self:
            if r.nivel_acceso > 10 or r.nivel_acceso < 1:
                raise ValidationError("Error, el nivel es del 1 al 10")