from odoo import _, api, fields, models

class Profesor(models.Model):
    _name = 'academia.profesor'
    _description = 'Profesor de la academia'

    name = fields.Char(string="Nombre del profesor", required=True)
    email = fields.Char(string="Correo del profesor")

    # Un profesor imparte varios cursos
    curso_ids = fields.One2many('academia.curso', 'profesor_id', string='Cursos asignados')
    
    # Cada profesor tiene un departamento
    departamento_id = fields.Many2one('academia.departamento', string='Departamento')