from odoo import models, fields, api, exceptions

class ExamData(models.Model):

    _name = 'exam.data'
    # student_id = fields.Many2many('attendance.data', )
    exam_id = fields.Integer('Exam ID', )
    _sql_constraints = [
        ('exam_id',
         'UNIQUE (exam_id)',
         'Exam ID must be unique!')]
    student_names = fields.Many2one('student.data',"Name")
    subject_names = fields.Many2one('subject.data')
    exam_marks = fields.Integer('Marks')
    exam_level = fields.Char('Exam Level')




    # school_class = fields.One2many('class.data', 'class_id', ondelete='set null', string='Class Name', index=True)
    # exam_student = fields.One2many('student.data', 'student_name')
    # exam_class = fields.Many2many('class.data', ondelete='set null', string="Class", index=True)
    # exam_subject = fields.Many2many('class.data', ondelete='set null', string="Subject", index=True)
    # exam_marks = fields.Char('Marks',)
    # exam_percent = fields.Char('Percentage', )
    #
    # @api.onchange('exam_marks')
    # def _onchange_name(self):
    #     for records in self:
    #         records.exam_percent = str(records.exam_marks)+'%'
    #     return