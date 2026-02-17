from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Persona(models.Model):
    _name = 'repaso_examen.persona'
    _description = 'Clase Persona'

    nombre = fields.Char(string='Nombre completo', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(compute='_compute_edad', string='Edad', store=True)
    
    rol = fields.Selection([
        ('estudiante', 'Estudiante'),
        ('trabajador', 'Trabajador'),
        ('jubilado', 'Jubilado')
    ], string='rol', default='estudiante', store=True)

    etapa_vida = fields.Selection([
        ('menor', 'Menor'),
        ('adulto', 'Adulto')
    ], string='etapa_vida', compute='_compute_etapa_vida', store=True)

    empresa_id = fields.Many2one('repaso_examen.empresa', string='Empresa')
    
    @api.depends('edad')
    def _compute_etapa_vida(self):
        for r in self:
            if r.edad < 18:
                r.etapa_vida = 'menor'
            else:
                r.etapa_vida = 'adulto'

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
                raise ValidationError("LA EDAD NO PUEDE SER NEGATIVA")