# -*- coding: utf-8 -*-

from odoo import models, fields


class wilson(models.Model):
     _name = 'wilson.vargas'
     _description = 'esta es la segunda base cap'

     nombre = fields.Char()
     apellido = fields.Char()
     monto = fields.Integer()
     #otro monto = fields.Float(compute="_value_pc", store=True)
     detalle = fields.Text()
        
    state = fields.Selection(selection=[
        ('draft', 'New'),
        ('approve', 'Approved'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),], string='State', default='draft')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
