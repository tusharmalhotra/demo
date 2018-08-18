from odoo import models, fields, api


class StudentWizard(models.TransientModel):
    _name = 'exam.wizard.data'

    # def _get_default_student(self):
    #     return self.env['student.data'].browse(self.env.context.get('student_subject'))
    #
    exam_ids = fields.Integer('Exam ID', default=1)
    _sql_constraints = [
        ('exam_ids',
         'UNIQUE (exam_ids  )',
         'Exam ID must be unique!')]
    student_names = fields.Many2one('student.data', string='Student Name')
    subject_names = fields.Many2one('subject.data', string='Subject Name')
    level = fields.Char('Level')
    marks = fields.Integer('Marks')

    @api.multi
    def set_student_level(self):
        self.env['exam.data'].create({'exam_id': self.exam_ids,
                                      'student_names': self.student_names.id,
                                      'subject_names': self.subject_names.id,
                                      'exam_marks': self.marks,
                                      'exam_level': self.level})



    # @api.multi
    # def set_marks(self):
    #     for rec in self:
    #         if rec.student_ids:
    #             for stud in rec.student_ids:
    #                 stud.exam_marks = self.marks




