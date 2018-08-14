from odoo import models, fields


class SubjectData(models.Model):
    _name = 'subject.data'
    subject_id = fields.Char('Subject Code', required=True)
    subject_name = fields.Char('Subject Name', required=True)


