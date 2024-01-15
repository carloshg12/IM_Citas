# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cita(models.Model):
    _name = 'imcitas.cita'
    _description = 'imcitas.cita'

    name = fields.Char()