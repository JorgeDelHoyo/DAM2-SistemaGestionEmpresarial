from odoo import _, api, fields, models

class Matricula(models.Model):
    _name = 'academia.matricula'
    _description = 'Matricula del alumno en un Curso'

    fecha_matricula = fields.Date(string="Fecha", default=fields.Date.context_today)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('validado', 'Validado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador')

    # Muchas matriculas pertenecen a un curso
    curso_id = fields.Many2one('academia.curso', string='Curso')

    alumno_id = fields.Many2one('academia.alumno', string='Alumno')