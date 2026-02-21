from odoo import _, api, fields, models

class Workplace(models.Model):
    _name = 'modulo_base.workplace'
    _description = 'Workplace Base'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Workplace', required=True)
    
    persona_ids = fields.One2many('modulo_base.persona', 'workplace_id', string='Personas')