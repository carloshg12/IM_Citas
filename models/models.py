# -*- coding: utf-8 -*-
from datetime import timedelta, time
from odoo import models, fields, api
from odoo.exceptions import ValidationError


# -- Jose -- #

class Cita(models.Model):
    _name = 'imcitas.cita'
    _description = 'imcitas.cita'

    name = fields.Char(string="Asunto de la cita", required=True)
    start_date = fields.Datetime(string="Hora de inicio", required=True)
    end_date = fields.Datetime("Hora de finalización")
    duration = fields.Float()
    cliente_id =  fields.Char(string="Cliente", required=True)  # A falta de cambiar cuando haga Iker su parte
    gestor_id = fields.Many2one('imcitas.gestor', string='Gestor', required=True)
    consultoria_id = fields.Many2many('imcitas.consultoria', string='Consultoría')

    @api.onchange('consultoria_id', 'start_date')
    def _onchange_consultoria_id(self):
        total_duration = 0
        if self.consultoria_id:
            for consultoria in self.consultoria_id:
                total_duration += consultoria.duration if consultoria.duration else 0

        self.duration = total_duration

        if self.start_date:
            duration_delta = timedelta(minutes=self.duration)
            self.end_date = self.start_date + duration_delta

    @api.constrains('start_date', 'end_date')
    def _check_time_range(self):
        start_time_boundary = time(8, 0)  # 9:00 AM  Pongo 8 provisionalmente por el GMT +1
        end_time_boundary = time(19, 0)  # 8:00 PM   Pongo 19 provisionalmente por el GMT +1

        for record in self:
            if record.start_date and record.end_date:
                start_time = record.start_date.time()
                end_time = record.end_date.time()

                if not (start_time_boundary <= start_time <= end_time_boundary):
                    raise ValidationError("La hora de inicio debe estar entre las 9:00 AM y las 8:00 PM.")

                if not (start_time_boundary <= end_time <= end_time_boundary):
                    raise ValidationError("La hora de finalización debe estar entre las 9:00 AM y las 8:00 PM.")

                if end_time < start_time:
                    raise ValidationError("La hora de finalización debe ser después de la hora de inicio.")


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

    name = fields.Char()






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


