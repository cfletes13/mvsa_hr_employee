# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    age = fields.Integer(
        string='Antiguedad',
        readonly=True,
        compute='_compute_age',
    )

    @api.multi
    @api.depends('x_studio_fecha_de_ingreso')
    def _compute_age(self):
        for record in self:
            age = 0
            if record.x_studio_fecha_de_ingreso:
                age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.x_studio_fecha_de_ingreso)).years
            record.age = age
