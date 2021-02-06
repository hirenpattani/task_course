# -*- coding: utf-8 -*-
from odoo import http


class TaskCourse(http.Controller):

    @http.route('/course', auth='public')
    def view_course(self, **kw):
        return http.request.render('task_course.website_course_list', {
            'courses': http.request.env['course.course'].sudo().search([])
        })
