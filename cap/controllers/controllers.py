# -*- coding: utf-8 -*-
# from odoo import http


# class Cap(http.Controller):
#     @http.route('/cap/cap/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cap/cap/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cap.listing', {
#             'root': '/cap/cap',
#             'objects': http.request.env['cap.cap'].search([]),
#         })

#     @http.route('/cap/cap/objects/<model("cap.cap"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cap.object', {
#             'object': obj
#         })
