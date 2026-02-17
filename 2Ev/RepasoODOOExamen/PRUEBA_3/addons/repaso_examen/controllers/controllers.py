# from odoo import http


# class RepasoExamen(http.Controller):
#     @http.route('/repaso_examen/repaso_examen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/repaso_examen/repaso_examen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('repaso_examen.listing', {
#             'root': '/repaso_examen/repaso_examen',
#             'objects': http.request.env['repaso_examen.repaso_examen'].search([]),
#         })

#     @http.route('/repaso_examen/repaso_examen/objects/<model("repaso_examen.repaso_examen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('repaso_examen.object', {
#             'object': obj
#         })

