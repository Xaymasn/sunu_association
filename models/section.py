# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Section(models.Model):
    _name = 'sunu_association.section'
    nom = fields.Char( string='Nom', required=True, )
    zoneGeographique = fields.Text(
        string='Zone Géographique',
        required=True,
    )
    
    