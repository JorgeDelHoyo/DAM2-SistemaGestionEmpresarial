from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Hospital(models.Model):
    _name = 'examen_hospital.hospital'
    _inherits = {
        'modulo_base.workplace':'workplace_id',
        'modulo_base.sleepplace' : 'sleepplace_id'}
    _description = 'Hospital hereda de Workplace y SleepPlace'
    _rec_name = 'name'

    paciente_ids = fields.One2many('examen_hospital.paciente', 'hospital_id', string='Pacientes')
    workplace_id = fields.Many2one('modulo_base.workplace', string='Workplace', required=True, ondelete='cascade')
    sleepplace_id = fields.Many2one('modulo_base.sleepplace', string='SleepPlace', required=True, ondelete='cascade')

    camas_libres = fields.Integer(compute='_compute_camas_libres', string='camas_libres')
    
    @api.depends('cantidad', 'paciente_ids')
    def _compute_camas_libres(self):
        for r in self:
            total_camas = r.cantidad or 0
            r.camas_libres = total_camas - len(r.paciente_ids)
            
    def action_alta_masiva(self):
        """Da de alta a todos los pacientes desvinculándolos del hospital"""
        for r in self:
            r.paciente_ids.write({'hospital_id': False})