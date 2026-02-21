from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'examen_empresa.empleado'
    _inherit = 'modulo_base.persona'
    _description = 'Empleado'
    _rec_name = 'name'

    empresa_id = fields.Many2one('examen_empresa.empresa', string='Empresa')
    fecha_contrato = fields.Date(string='Fecha de Contrato')
    puesto = fields.Char(string='Puesto')

    email = fields.Char(compute='_compute_email', string='email', store=True)
    
    @api.depends('name')
    def _compute_email(self):
        for r in self:
            if r.name:
                nombre_limpio = r.name.lower().replace(" ",".")
                r.email = f"{nombre_limpio}@empresa.com"
            else:
                r.email = False
    
    @api.constrains('edad')
    def _constrains_edad(self):
        for r in self:
            if r.edad < 16:
                raise ValidationError("Un empleado no puede tener menos de 16 años")
    
    def action_cambiar_puesto(self, nuevo_puesto):
        self.ensure_one() # Asegura que solo lo aplicamos a un empleado
        self.puesto = nuevo_puesto