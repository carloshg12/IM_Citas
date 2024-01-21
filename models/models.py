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
    cliente_id =  fields.Many2one('imcitas.cliente',string="Cliente", required=True) 
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
                
    @api.constrains('start_date', 'end_date', 'gestor_id')
    def _check_gestor_availability(self):
        for record in self:
            if not (record.start_date and record.end_date and record.gestor_id):
                continue  # Si falta alguna información, no realizar la comprobación

            # Buscar otras citas con el mismo gestor en el mismo rango de tiempo
            overlapping_citas = self.search([
                ('id', '!=', record.id),  # Excluir la cita actual
                ('gestor_id', '=', record.gestor_id.id),  # Mismo gestor
                ('start_date', '<', record.end_date),  # Comienza antes de que termine esta cita
                ('end_date', '>', record.start_date)  # Termina después de que comience esta cita
            ])

            if overlapping_citas:
                raise ValidationError("Ya existe una cita con este gestor en el mismo rango de tiempo.")
            


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


