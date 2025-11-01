# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class osama_saudi(models.Model):
#     _name = 'osama_saudi.osama_saudi'
#     _description = 'osama_saudi.osama_saudi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

