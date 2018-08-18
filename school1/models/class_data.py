from odoo import models, fields, api


class ClassData(models.Model):
    _name = 'class.data'

    class_id = fields.Integer('Class ID')
    # _sql_constraints = [
    #     ('class_id',
    #      'UNIQUE (class_id)',
    #      'Class ID must be unique!')]
    name = fields.Char('Class name')
    class_room = fields.Char('Room Number',)
    class_subject = fields.Many2many('subject.data' )
    class_teacher = fields.Many2many('hr.employee')

