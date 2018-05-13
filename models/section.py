# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Section(models.Model):
    _name = 'sunuAssociation.section'
    nom = fields.Char( string='Nom', required=True, )
    zoneGeographique = fields.Text(
        string='Zone Géographique',
        required=True,
    )
    
    