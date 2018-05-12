# -*- coding: utf-8 -*-
from odoo import http

# class SunuAssociation(http.Controller):
#     @http.route('/sunu_association/sunu_association/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sunu_association/sunu_association/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sunu_association.listing', {
#             'root': '/sunu_association/sunu_association',
#             'objects': http.request.env['sunu_association.sunu_association'].search([]),
#         })

#     @http.route('/sunu_association/sunu_association/objects/<model("sunu_association.sunu_association"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sunu_association.object', {
#             'object': obj
#         })