from odoo import models, fields, api

class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Curso academico'

    name = fields.Char(string="Nombre del curso", required=True)
    creditos = fields.Float(string="Creditos del curso")

    # Muchos cursos pueden ser impartidos por muchos profesores
    profesor_ids = fields.Many2many('academia.profesor','curso_profesor_rel', string='Profesores Asignados')

    # Un curso puede tener varias matriculas de alumnos
    matricula_ids = fields.One2many('academia.matricula', 'curso_id', string='Matriculas')