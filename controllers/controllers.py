# -*- coding: utf-8 -*-
# from odoo import http


# class Imcitas(http.Controller):
#     @http.route('/imcitas/imcitas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/imcitas/imcitas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('imcitas.listing', {
#             'root': '/imcitas/imcitas',
#             'objects': http.request.env['imcitas.imcitas'].search([]),
#         })

#     @http.route('/imcitas/imcitas/objects/<model("imcitas.imcitas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('imcitas.object', {
#             'object': obj
#         })
