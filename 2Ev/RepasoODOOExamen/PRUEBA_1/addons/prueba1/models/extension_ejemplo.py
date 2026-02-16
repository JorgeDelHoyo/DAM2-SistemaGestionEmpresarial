from odoo import _, api, fields, models

class ExtensionEmpresa(models.Model):
    _inherit = 'prueba1.empresa' # no tiene _name nuevo
    _description = 'ExtensionEmpresa'

    es_multinacional = fields.Boolean(string='¿Es Multinacional?')
    