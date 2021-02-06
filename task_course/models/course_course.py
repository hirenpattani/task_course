# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class CourseCourse(models.Model):
    _name = "course.course"
    _description = "Courses"

    name = fields.Char(required=True)
    description = fields.Text()
    instructor_id = fields.Many2one("hr.employee", required=True)
    room_id = fields.Many2one("room.room", required=True)
    attendees_ids = fields.Many2many(
        "res.partner",
        "course_partner_rel",
        "course_id",
        "partner_id",
        string="Attendees",
    )
    lession_ids = fields.One2many("course.lession.line", "course_id", string="Lessions")

    @api.constrains("instructor_id", "attendees_ids", "lession_ids")
    def _constrains_instructor(self):
        for course in self:
            if course.instructor_id.user_partner_id.id in course.attendees_ids.ids:
                raise ValidationError(_("Instructor can't be added as Attendee"))
            if len(course.attendees_ids) > course.room_id.max_attendees:
                raise ValidationError(
                    _("Number of Attendees exceeded the Capacity of room")
                )


class CourseLessionLine(models.Model):
    _name = "course.lession.line"
    _description = "Course Lession Line"

    course_id = fields.Many2one("course.course")
    lession_id = fields.Many2one(
        "lession.lession",
        required=True,
    )
    room_id = fields.Many2one("room.room", related="lession_id.room_id")
