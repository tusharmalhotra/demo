from odoo import models, fields


class SubjectData(models.Model):
    _name = 'subject.data'
    subject_id = fields.Integer('Subject Code',)
    _sql_constraints = [
        ('subject_id',
         'UNIQUE (subject_id)',
         'Subject ID must be unique!')]
    name = fields.Char('Subject Name')


