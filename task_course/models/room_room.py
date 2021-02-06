# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class RoomRoom(models.Model):
    _name = "room.room"
    _description = "Rooms"

    name = fields.Char(required=True)
    location = fields.Char()
    capacity = fields.Integer(string="Room Capacity", required=True)
    max_attendees = fields.Integer(string="No. of Attendees", required=True)
