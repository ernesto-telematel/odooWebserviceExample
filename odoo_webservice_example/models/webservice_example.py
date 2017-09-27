# -*- coding: utf-8 -*-

from odoo import models, fields, api

from suds.client import Client

class WebServiceModel(models.Model):
    _name = "webservice.model"

    name = fields.Char("Liga de servicio a consultar")
    result = fields.Text("Resultado")
    method_call = fields.Char("Nombre de metodo")
    parameters_ids = fields.One2many("webservice.params", "webservice_id")


    @api.model
    def method_basic_example(self):
        return "Webservice consultado!"

    @api.multi
    def call_another_webservice(self):
        for record in self:
            client = Client(record.name)
            dict_parameters = {}
            for argument in self.parameters_ids:
                dict_parameters[argument.name] = argument.send_data
            import pdb; pdb.set_trace()
            result = getattr(client.service, record.method_call)(**dict_parameters)
            record.result = result

class WebServiceModelParams(models.Model):
    _name = "webservice.params"

    name = fields.Char("Nombre de parametro")
    send_data = fields.Char("Valor a enviar")
    webservice_id = fields.Many2one("webservice.model")
