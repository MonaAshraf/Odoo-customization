# -*- coding: utf-8 -*-
from openerp import http

# class My-addons(http.Controller):
#     @http.route('/my-addons/my-addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-addons/my-addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-addons.listing', {
#             'root': '/my-addons/my-addons',
#             'objects': http.request.env['my-addons.my-addons'].search([]),
#         })

#     @http.route('/my-addons/my-addons/objects/<model("my-addons.my-addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-addons.object', {
#             'object': obj
#         })