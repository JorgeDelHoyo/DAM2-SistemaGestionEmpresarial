from odoo import models, fields, api

class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Curso academico'

    name = fields.Char(string="Nombre del curso", required=True)
    creditos = fields.Float(string="Creditos del curso")

    # Muchos cursos pueden ser impartidos por un profesor
    profesor_id = fields.Many2one('academia.profesor', string='Profesor principal')

    # Un curso puede tener varias matriculas de alumnos
    matricula_ids = fields.One2many('academia.matricula', 'curso_id', string='Matriculas')