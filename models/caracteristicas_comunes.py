from odoo import models, fields

class CaracteristicasComunes(models.AbstractModel):
    _name = "modelo_abstract"
    _description = "un modelo para campos temporales"

    Peso = fields.Char(string="Peso", readonly=True)
    Peso_valor = fields.Char(string="30kg")

