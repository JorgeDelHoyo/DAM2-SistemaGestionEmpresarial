from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Nave(models.Model):
    _name = 'starwars.nave'
    _description = 'Nave'

    name = fields.Char(string="Identificador de la nave")
    tipo_id = fields.Many2one('starwars.tipo.nave', string='Tipo Nave', required=True)
    piloto_id = fields.Many2one('starwars.piloto', string='Pilotos')
    estado = fields.Selection([
        ('operativa', 'Operativa'),
        ('dañada', 'Dañada'),
        ('enMantenimiento', 'En Mantenimiento')
    ], string='Estado de la nave')
    escudos = fields.Integer(string='Escudos de la nave (0 a 100)')

    mision_ids = fields.Many2many('starwars.mision', string='Misiones realizadas')

    @api.constrains('escudos')
    def _check_escudos(self):
        for nave in self:
            if nave.escudos > 100 or nave.escudos < 0:
                raise ValidationError("Error!, Los escudos deben estar entre 0 y 100")
    