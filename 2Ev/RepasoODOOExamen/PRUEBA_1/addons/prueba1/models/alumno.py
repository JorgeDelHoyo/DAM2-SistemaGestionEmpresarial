from odoo import _, api, fields, models

class Alumno(models.Model):
    _name = 'prueba1.alumno'
    _inherit = 'prueba1.persona' # Hereda de la clase Persona
    _description = 'Alumno'

    curso_escolar = fields.Char(string='Curso actual')

    # Relación: Un alumno pertenece a una empresa de prácticas
    empresa_id = fields.Many2one('prueba1.empresa', string='Empresa Asignada')