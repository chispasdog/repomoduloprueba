from odoo import models, fields

class ModeloSimple(models.Model):
    _name = "modelo_simple"
    _description = "Campo de texto largo para descripciones."

    active = fields.Boolean(string="Active", required=True)
