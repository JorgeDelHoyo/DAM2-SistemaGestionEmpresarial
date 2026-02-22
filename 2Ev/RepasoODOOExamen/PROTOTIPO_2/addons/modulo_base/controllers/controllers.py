# from odoo import http


# class ModuloBase(http.Controller):
#     @http.route('/modulo_base/modulo_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_base/modulo_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_base.listing', {
#             'root': '/modulo_base/modulo_base',
#             'objects': http.request.env['modulo_base.modulo_base'].search([]),
#         })

#     @http.route('/modulo_base/modulo_base/objects/<model("modulo_base.modulo_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_base.object', {
#             'object': obj
#         })

