from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Paciente(models.Model):
    _name = 'examen_hospital.paciente'
    _inherit = 'modulo_base.persona'
    _description = 'Paciente'
    _rec_name = 'name'

    hospital_id = fields.Many2one('examen_hospital.hospital', string='Hospital')
    gravedad = fields.Selection([
        ('leve', 'Leve'),
        ('grave','Grave')
    ], string='Estado del Paciente')

    # AÑADE ESTO EN PACIENTE.PY
    @api.constrains('hospital_id')
    def _check_aforo_hospital(self):
        for record in self:
            # Si el paciente va a un hospital y las camas quedan por debajo de 0
            if record.hospital_id and record.hospital_id.camas_libres < 0:
                raise ValidationError("¡Error! No hay camas suficientes para tantos pacientes.")