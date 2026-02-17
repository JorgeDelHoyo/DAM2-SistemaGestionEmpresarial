from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Persona(models.Model):
    _name = 'prueba1.persona'
    _description = 'Clase Base Persona'

    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(compute='_compute_edad', string='edad', store=True)

    rol = fields.Selection([
        ('estudiante', 'Estudiante'),
        ('trabajador', 'Trabajador'),
        ('jubilado', 'Jubilado')
    ], string='rol', default='estudiante')
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for r in self:
            if r.fecha_nacimiento:
                hoy = date.today()
                r.edad = hoy.year - r.fecha_nacimiento.year
            else:
                r.edad = 0
    
    @api.constrains('edad')
    def _constrains_edad(self):
        for r in self:
            if r.edad < 0:
                raise ValidationError("La edad no puede ser negativa")


    etapa = fields.Selection([
        ('menor', 'Menor'),
        ('adulto', 'Adulto')
    ], string='etapa', compute='_compute_etapa', store=True)

    @api.depends('edad')
    def _compute_etapa(self):
        for r in self:
            if r.edad < 18:
                r.etapa = 'menor'
            else:
                r.etapa = 'adulto'