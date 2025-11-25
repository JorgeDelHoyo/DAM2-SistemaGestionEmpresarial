from odoo import _, api, fields, models

class Mision(models.Model):
    _name = 'starwars.mision'
    _description = 'Misiones'

    name = fields.Char(string='Nombre de la mision')
    fecha = fields.Date(string='Fecha')
    nave_ids = fields.Many2many('starwars.nave', string='Naves que participan')

    puntos_totales = fields.Char(compute='_calcula_fuerza', string='Puntos totales')
    
    @api.depends('nave_ids')
    def _calcula_fuerza(self):
        for mision in self:
            suma = 0

            for nave in mision.nave_ids:
                suma = suma + nave.escudos
            
            mision.puntos_totales = suma
    