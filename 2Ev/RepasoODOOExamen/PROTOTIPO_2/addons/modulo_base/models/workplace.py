from odoo import _, api, fields, models

class WorkPlace(models.Model):
    _name = 'modulo_base.workplace'
    _description = 'WorkPlace'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Workplace', required=True)
    aforo_base = fields.Integer(string='Aforo Base')


    persona_ids = fields.One2many('modulo_base.persona', 'workplace_id', string='Personas')