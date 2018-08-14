from odoo import models,fields

class class_data(models.Model):
    _name = 'class.data'

    class_id = fields.Many2many('subject.data', string="Subject")
    room_no = fields.Char('Room Number', required=True)
    class_name = fields.Char('Class Name', required=True)

     # @api.depends('subject_id')
     # def get_subject(self):
     # for rec in self:
     #    subject_id = ','.join(subject_id for journal in rec.subject_id)
     #    rec.subject_id = subject_id