from odoo import _, api, fields, models

class Evento(models.Model):
    _name = 'prueba4.evento'
    _description = 'Evento'
    _inherit = 'prueba4.recinto'
    _rec_name = 'nombre'
    
    fecha_inicio = fields.Date(string='Fecha Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha Fin', required=True)
    tipo = fields.Selection([
        ('musical', 'Musical'),
        ('deportivo', 'Deportivo'),
        ('corporativo', 'Corporativo')
    ], string='Tipo de Evento')

    # Un evento tiene muchos asistentes asociados
    asistente_ids = fields.One2many('prueba4.asistente', 'evento_id', string='Asistentes')

    plazas_disponibles = fields.Integer(compute='_compute_plazas_disponibles', string='Plazas Disponibles', store=True)
    
    # Campo calculado que resta a la cantidad_maxima el numeor de asistentes apuntados
    @api.depends('capacidad_maxima')
    def _compute_plazas_disponibles(self):
        for r in self:
            r.plazas_disponibles = r.capacidad_maxima - len(r.asistente_ids)