# from odoo import models, fields, api


# class prueba4(models.Model):
#     _name = 'prueba4.prueba4'
#     _description = 'prueba4.prueba4'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

