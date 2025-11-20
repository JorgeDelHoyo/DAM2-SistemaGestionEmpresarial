from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Curso academico'

    name = fields.Char(string="Nombre del curso", required=True)
    creditos = fields.Float(string="Creditos del curso")

    # Muchos cursos pueden ser impartidos por muchos profesores
    profesor_ids = fields.Many2many('academia.profesor','curso_profesor_rel', string='Profesores Asignados')

    # Un curso puede tener varias matriculas de alumnos
    matricula_ids = fields.One2many('academia.matricula', 'curso_id', string='Matriculas')

    @api.constrains('creditos')
    def _check_creditos_positivos(self):
        for record in self:
            if record.creditos < 0:
                raise ValidationError("LOS CRÉDITOS NO PUEDEN SER NEGATIVOS")