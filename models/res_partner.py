from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'

    followers = fields.Integer(string='followers')
    following = fields.Integer(string='following')
    social_media_profile_link = fields.Char(string='social_media_profile_link')
    last_post_date = fields.Datetime(string='last_post_date')
    post_count = fields.Integer(string='post_count')
    likes_recieved = fields.Integer(string='likes_received')
    comments_received = fields.Integer(string='comments_received')

    def compute_sum_followers(self):
        self.followers += 1
