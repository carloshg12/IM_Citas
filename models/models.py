# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api


# -- Jose -- #

class Cita(models.Model):
    _name = 'imcitas.cita'
    _description = 'imcitas.cita'

    name = fields.Char()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    duration = fields.Float()
    consultoria_id = fields.Many2many('imcitas.consultoria', string='Consultoría')

    @api.onchange('consultoria_id', 'start_date')
    def _onchange_consultoria_id(self):
            total_duration = 0
            for consultoria in self.consultoria_id:
                total_duration += consultoria.duration

            self.duration = total_duration

            if self.start_date:
                # Convertir la duración total en minutos
                duration_delta = timedelta(minutes=self.duration)
                self.end_date = self.start_date + duration_delta


# -- Carlos -- #

class Calculadora(models.Model):
    _name = 'imcitas.calculadora'
    _description = 'imcitas.calculadora'

    name = fields.Char()
    consultoria_ids = fields.Many2many('imcitas.consultoria', string='Consultorías')
    total_duration = fields.Integer(string="Duración Total", compute="_calculate_totals")
    total_cost = fields.Float(string="Costo Total", compute="_calculate_totals")

    @api.depends('consultoria_ids', 'consultoria_ids.duration', 'consultoria_ids.cost')
    def _calculate_totals(self):
        for record in self:
            record.total_duration = sum(consultoria.duration for consultoria in record.consultoria_ids)
            record.total_cost = sum(consultoria.cost for consultoria in record.consultoria_ids)





# -- Iker -- #

class Cliente(models.Model):
    _name = 'imcitas.cliente'
    _description = 'imcitas.cliente'

    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellidos")
    email = fields.Char(string="Correo Electrónico")
    phone = fields.Char(string="Teléfono")
    street = fields.Char(string="Calle")
    country = fields.Char(string="País")
    city = fields.Char(string="Ciudad")
    photo = fields.Binary(string='Foto')




# -- Carlos y Jose -- #

class Consultoria(models.Model):
    _name = 'imcitas.consultoria'
    _description = 'imcitas.consultoria'

    name = fields.Char(string="Tipo de cita",required=True)
    duration = fields.Integer()
    cost = fields.Float()

class Gestor(models.Model):
    _name = 'imcitas.gestor'
    _description = 'imcitas.gestor'

    name = fields.Char()


