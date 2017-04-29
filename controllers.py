# -*- coding: utf-8 -*-
from openerp import http

# class Tritel(http.Controller):
#     @http.route('/tritel/tritel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tritel/tritel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tritel.listing', {
#             'root': '/tritel/tritel',
#             'objects': http.request.env['tritel.tritel'].search([]),
#         })

#     @http.route('/tritel/tritel/objects/<model("tritel.tritel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tritel.object', {
#             'object': obj
#         })