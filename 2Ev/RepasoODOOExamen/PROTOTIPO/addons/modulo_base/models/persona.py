from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class Persona(models.Model):
    _name = 'modulo_base.persona'
    _description = 'Persona Base'
    _rec_name = 'name'

    name = fields.Char(string='Nombre de la persona', required=True)

    workplace_id = fields.Many2one('modulo_base.workplace', string='Workplace')

    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(compute='_compute_edad', string='edad', store=True)
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for r in self:
            if r.fecha_nacimiento:
                hoy = date.today()
                r.edad = hoy.year - r.fecha_nacimiento.year
            else:
                r.edad = -1
    
    @api.constrains('edad')
    def _constrains_edad(self):
        for r in self:
            if r.edad < 0:
                raise ValidationError("La edad no puede ser menor que 0 (cambia la fecha de nacimiento)")