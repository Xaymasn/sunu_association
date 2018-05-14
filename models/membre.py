# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Membre(models.Model):
    _inherit = 'res.partner'
    prenom = fields.Char(string='Prénom', required=True,)
    nom = fields.Char(string='Nom',required=True,)
    telephone = fields.Char(string='Téléphone',required=True,)
    image = fields.Binary(string='Image' )
    adresse = fields.Char(string='Adresse')
    courriel = fields.Char(string='Courriel') 
    