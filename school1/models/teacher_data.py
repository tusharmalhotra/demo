from odoo import fields, models

class Employee(models.Model):
    # _name = 'teacher.data'
    _inherit = 'hr.employee'

    teacher_id = fields.Integer('Teacher ID')
    _sql_constraints = [
        ('teacher_id',
         'UNIQUE (teacher_id)',
         'Teacher ID must be unique!')]
    name = fields.Char('Teacher Name')
    teacher_age = fields.Integer('age')
    teacher_class = fields.Many2many('class.data')
    teacher_subject = fields.Many2many('subject.data')

