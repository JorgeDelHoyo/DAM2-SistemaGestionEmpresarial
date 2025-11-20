from odoo import _, api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class Alumno(models.Model):
    _name = 'academia.alumno'
    _description = 'Alumno de la academia'
    
    name = fields.Char(string="Nombre del alumno", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")

    es_mayor_edad = fields.Boolean(compute='_compute_mayor_edad', string='Mayor de edad(+18)')
    
    # Comprueba mediante la fecha de nacimiento introducida si es mayor de edad o no
    @api.depends('fecha_nacimiento')
    def _compute_mayor_edad(self):
        hoy = date.today()
        for record in self:
            if record.fecha_nacimiento:
                # Calcular la edad para la validacion
                age = relativedelta(hoy, record.fecha_nacimiento).years

                # Asignar valor boolean
                record.es_mayor_edad = (age >= 18)
            else:
                # Si la fecha no esta no es mayor de edad
                record.es_mayor_edad = False

    # Un alumno tiene varias matriculas
    matricula_ids = fields.One2many('academia.matricula', 'alumno_id', string='Matriculas alumno')