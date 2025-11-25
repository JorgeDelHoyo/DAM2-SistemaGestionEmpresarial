# from odoo import http


# class Starwars(http.Controller):
#     @http.route('/starwars/starwars', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/starwars/starwars/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('starwars.listing', {
#             'root': '/starwars/starwars',
#             'objects': http.request.env['starwars.starwars'].search([]),
#         })

#     @http.route('/starwars/starwars/objects/<model("starwars.starwars"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('starwars.object', {
#             'object': obj
#         })

