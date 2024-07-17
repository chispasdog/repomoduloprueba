from odoo import models, fields

class DatosTemporales(models.TransientModel):
    _name = "modelo_transient"
    _description = "un modelo para campos temporales"

    session_id = fields.Char(string="id de sesion", readonly=True)
    data = fields.Text(string="Datos temporales almacenados.")
    date_created = fields.Datetime(string="fecha de creacion de registros")
