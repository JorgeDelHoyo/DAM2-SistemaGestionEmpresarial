from odoo import _, api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class Alumno(models.Model):
    _name = 'academia.alumno'
    _description = 'Alumno de la academia'
    
    name = fields.Char(string="Nombre del alumno", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")

    # Calcular la edad
    edad_actual = fields.Char(compute='_compute_edad_actual', string='Edad')
    
    # Compute para calcular la edad
    @api.depends('fecha_nacimiento')
    def _compute_edad_actual(self):
        today = date.today()
        for record in self:
            if record.fecha_nacimiento:
                age = relativedelta(today, record.fecha_nacimiento).years
                record.edad_actual = "f{age} años"
            else:
                record.edad_actual = "Fecha no definida"

    # Un alumno tiene varias matriculas
    matricula_ids = fields.One2many('academia.matricula', 'alumno_id', string='Matriculas alumno')