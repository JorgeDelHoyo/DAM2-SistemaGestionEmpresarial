# from odoo import http


# class Prueba4(http.Controller):
#     @http.route('/prueba4/prueba4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba4/prueba4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba4.listing', {
#             'root': '/prueba4/prueba4',
#             'objects': http.request.env['prueba4.prueba4'].search([]),
#         })

#     @http.route('/prueba4/prueba4/objects/<model("prueba4.prueba4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba4.object', {
#             'object': obj
#         })

