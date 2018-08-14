from odoo import models,fields

class subject_data(models.Model):
    _name = 'subject.data'

    subject_id = fields.Many2many('class.data', ondelete='set null', string="Class", index=True)
    subject_name = fields.Char(string = "Subject")
