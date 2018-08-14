from odoo import models, fields


class ClassData(models.Model):
    _name = 'class.data'
    class_id = fields.Char('Class ID', required=True)
    class_room = fields.Char('Room Number', required=True)
    class_subject = fields.Char('subject', required=True)

