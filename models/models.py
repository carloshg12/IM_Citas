# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cita(models.Model):
    _name = 'imcitas.cita'
    _description = 'imcitas.cita'

    name = fields.Char()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    duration = fields.Float()