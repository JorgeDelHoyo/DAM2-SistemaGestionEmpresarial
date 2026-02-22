# from odoo import http


# class ExamenHospital(http.Controller):
#     @http.route('/examen_hospital/examen_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_hospital/examen_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_hospital.listing', {
#             'root': '/examen_hospital/examen_hospital',
#             'objects': http.request.env['examen_hospital.examen_hospital'].search([]),
#         })

#     @http.route('/examen_hospital/examen_hospital/objects/<model("examen_hospital.examen_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_hospital.object', {
#             'object': obj
#         })

