from odoo import _, api, fields, models

class Asistente(models.Model):
    _name = 'prueba4.asistente'
    _description = 'Asistente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre del asistente', required=True)
    dni = fields.Char(string='DNI', required=True)

    # Muchos asistentes, asisten a un evento
    evento_id = fields.Many2one('prueba4.evento', string='Evento', ondelete='cascade')