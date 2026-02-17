# from odoo import models, fields, api


# class repaso_examen(models.Model):
#     _name = 'repaso_examen.repaso_examen'
#     _description = 'repaso_examen.repaso_examen'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

