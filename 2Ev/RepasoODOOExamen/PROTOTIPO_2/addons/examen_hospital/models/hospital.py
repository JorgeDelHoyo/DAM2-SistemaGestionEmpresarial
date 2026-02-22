from odoo import _, api, fields, models

class Hospital(models.Model):
    _name = 'examen_hospital.hospital'
    _inherits = {
        'modulo_base.workplace':'workplace_id',
        'modulo_base.sleepplace':'sleepplace_id'}
    _description = 'Hospital'
    _rec_name = 'name'

    workplace_id = fields.Many2one('modulo_base.workplace', string='Workplace', required=True, ondelete='cascade')
    sleepplace_id = fields.Many2one('modulo_base.sleepplace', string='SleepPlace', required=True, ondelete='cascade')    

    paciente_ids = fields.One2many('examen_hospital.paciente', 'hospital_id', string='Pacientes')

    camas_libres = fields.Integer(compute='_compute_camas_libres', string='camas_libres')
    
    @api.depends('cantidad_camas', 'paciente_ids')
    def _compute_camas_libres(self):
        for r in self:
            r.camas_libres = r.cantidad_camas - len(r.paciente_ids)