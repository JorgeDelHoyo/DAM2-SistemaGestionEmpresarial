from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'examen_empresa.empleado'
    _inherit = 'modulo_base.persona'
    _description = 'Empleado'
    _rec_name = 'name'

    fecha_contrato = fields.Date(string='Fecha de contratacion')
    empresa_id = fields.Many2one('examen_empresa.empresa', string='Empresa')

    puesto = fields.Selection([
        ('junior', 'Junior'),
        ('mid','Mid'),
        ('senior','Senior')
    ], string='puesto', compute='_compute_puesto', default='junior', store=True)
    
    email = fields.Char(compute='_compute_email', string='email')

    @api.depends('edad')
    def _compute_puesto(self):
        for r in self:
            if r.edad < 21:
                r.puesto = 'junior'
            elif r.edad < 32 and r.edad > 20:
                r.puesto = 'mid'
            else:
                r.puesto = 'senior'
    
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
                raise ValidationError("No puede tener menos de 16 un trabajador")