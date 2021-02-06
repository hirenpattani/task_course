# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _compute_instructor_id(self):
        for partner in self:
            partner.instructor_id = self.env["hr.employee"].search(
                [("user_partner_id", "=", partner.id)], limit=1
            ).id

    instructor_id = fields.Many2one("hr.employee", compute="_compute_instructor_id")
    course_ids = fields.Many2many(
        "course.course",
        "course_partner_rel",
        "partner_id",
        "course_id",
        string="Courses",
    )
