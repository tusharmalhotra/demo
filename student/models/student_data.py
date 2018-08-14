from odoo import models,fields

class student_data(models.Model):
    _name = 'student.data'

    student_name = fields.Char('Name', required=True)
    class_ids = fields.Many2one('class.data', ondelete='set null', string="Class", index=True)
    subject = fields.Many2many('class.data', ondelete='set null', string="Subject", index=True)
    address = fields.Char('Address', required=True)
    city = fields.Char('City', required=True)
    state = fields.Char('State', required=True)
    zip_code = fields.Char('Zip Code', required=True)
    date_of_birth = fields.Date('Date of Birth')

