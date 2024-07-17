from odoo import models, fields

class res_users_aditionalinfo(models.Model):
    _inherit = 'res.users'

    age = fields.Integer(string='Edad')
    birthdate = fields.Date(string='Fch_nacimiento')
    is_active = fields.Boolean(string='esta_activo')
