from odoo import _, api, fields, models

class Sindicalista(models.Model):
    _name = 'repaso_examen.sindicalista'
    _description = 'Clase sindicalista delegacion'
    
    _inherits = {'repaso_examen.trabajador': 'trabajador_id'}

    trabajador_id = fields.Many2one('repaso_examen.trabajador', string='trabajador', required=True, ondelete='cascade')
    seccion_sindical = fields.Char(string='Sección Sindical')