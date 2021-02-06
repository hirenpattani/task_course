# -*- coding: utf-8 -*-
{
    "name": "Course",
    "summary": """
        course management,
        education management system,
        online courses,
    """,
    "description": """
        Manage courses and Attendees.
    """,
    "author": "Hiren Pattani",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    "depends": ["hr", "contacts", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/views_course_course.xml",
        "views/views_room_room.xml",
        "views/views_lession_lession.xml",
        "views/views_res_partner.xml",
        "report/report_course_course.xml",
    ],
    "application": True,
}
