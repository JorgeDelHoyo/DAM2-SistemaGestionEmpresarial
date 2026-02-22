from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class Persona(models.Model):
    _name = 'modulo_base.persona'
    _description = 'Persona'
    _rec_name = 'name'

    name = fields.Char(string='name', required=True)

    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')

    edad = fields.Integer(compute='_compute_edad', string='edad',store=True)

    workplace_id = fields.Many2one('modulo_base.workplace', string='WorkPlace')
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for r in self:
            if r.fecha_nacimiento:
                hoy = date.today()
                r.edad = hoy.year - r.fecha_nacimiento.year
            else:
                r.edad = 0
    
    @api.constrains('edad')
    def _check_edad(self):
        for r in self:
            if r.edad < 0:
                raise ValidationError("ERROR, la fecha no puede ser negativa")