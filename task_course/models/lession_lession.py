# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class LessionLession(models.Model):
    _name = "lession.lession"
    _description = "Lessions"

    name = fields.Char(required=True)
    room_id = fields.Many2one('room.room', required=True)
