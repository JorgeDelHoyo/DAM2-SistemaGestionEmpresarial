from odoo import _, api, fields, models

class Empresa(models.Model):
    _name = 'repaso_examen.empresa'
    _inherit = 'repaso_examen.negocio'
    _description = 'Clase Empresa hereda de Negocio'
    
    sector = fields.Char(string='Sector')

    # Relación para ver a sus trabajadores/alumnos
    persona_ids = fields.One2many('repaso_examen.persona', 'empresa_id', string='Personal')

class Multinacional(models.Model):
    _inherit = 'repaso_examen.empresa'
    _description = 'Es multinacional'

    es_multinacional = fields.Boolean(string='¿Es multinacional?')