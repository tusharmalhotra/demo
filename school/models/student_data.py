from odoo import models, fields


class StudentData(models.Model):
    _name = 'student.data'
    student_id = fields.Char('ID', required=True)
    student_name = fields.Char('Name', required=True)
    student_class = fields.Char('Class Name', required=True)
    student_address = fields.Char('Address', required=True)
    student_state = fields.Char('State', required=True)
    student_city = fields.Char('City', required=True)
    student_zip = fields.Char('ZIP Code', required=True)
