from odoo import _, api, fields, models

class Piloto(models.Model):
    _name = 'starwars.piloto'
    _description = 'Piloto'

    name = fields.Char(string="Nombre del piloto")
    edad = fields.Integer(string="Edad")

    bando_id = fields.Many2one('starwars.bando', string='Bandos')
    planeta_id = fields.Many2one('starwars.planeta', string='Planetas')
    rango_id = fields.Many2one('starwars.rango', string='Rangos')

    @api.onchange('edad')
    def _aviso_edad(self):
        if self.edad < 18:
            return{
                'warning': {
                    'tittle': "Cuidado",
                    'message': "Este piloto es muy joven, ten cuidado"
                }
            }
    