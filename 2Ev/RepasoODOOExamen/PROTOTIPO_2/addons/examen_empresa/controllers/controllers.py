# from odoo import http


# class ExamenEmpresa(http.Controller):
#     @http.route('/examen_empresa/examen_empresa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_empresa/examen_empresa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_empresa.listing', {
#             'root': '/examen_empresa/examen_empresa',
#             'objects': http.request.env['examen_empresa.examen_empresa'].search([]),
#         })

#     @http.route('/examen_empresa/examen_empresa/objects/<model("examen_empresa.examen_empresa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_empresa.object', {
#             'object': obj
#         })

