from odoo import models, fields, api, exceptions


class StudentData(models.Model):

    _name = 'student.data'

    student_id = fields.Integer('ID',)
    _sql_constraints = [
        ('student_id',
         'UNIQUE (student_id)',
         'Student ID must be unique!')]
    name = fields.Char('Student Name', ondelete='set null')
    student_class = fields.Many2one('class.data', ondelete='set null', string="Class Name", index=True)
    student_subject = fields.Many2many('subject.data', ondelete='set null', string="Subject Name", index=True)
    student_phone = fields.Integer('Phone Number',)
    student_address = fields.Char('Address')
    student_state = fields.Char('State')
    student_city = fields.Char('City')
    student_zip = fields.Integer('ZIP Code', size=6)
    student_level = fields.Char('Student Level')

    # @api.depends('student_city','student_name')
    # def _get_class(self):
    #     clas = str(self.student_city)
    #     nam = str(self.student_name)
    #     # self.inc = self.inc + 1
    #     for rec in self:
    #         newid = clas[0] + nam[0] + str(self.id)
    #         rec.student_id = newid

    # @api.onchange('student_name')
    # def _onchange_name(self):
    #     for records in self:
    #         na = records.student_name
    #         if str(na).startswith('a') or str(na).startswith('e') or str(na).startswith('i') or str(na).startswith('o') or str(na).startswith('u'):
    #             if records.student_id == 5:
    #                 records.student_id = 1
    #             else:
    #                 records.student_id = records.student_id + 1
    #     return


    # @api.constrains('student_id')
    # def check_id(self):
    #     """ make sure id is less then 50 or not"""
    #     for rec in self:
    #         if 22 > int(rec.student_id) and int(rec.student_id) < 50:
    #             raise exceptions.ValidationError(_('You are not allowed to enter the value more the 50'))
    #     return

    # @api.constrains('student_class')
    # def check_id(self):
    #     """ make sure id is less then 50 or not"""
    #     for rec in self.student_class:
    #         if int(self.student_class) < 15:
    #             raise exceptions.ValidationError(_('You are not allowed to enter the value more the 50'))
    #     return True

    # @api.constrains('student_phone')
    # def is_phone(self, cr, uid, ids, context=None):
    #     record = self.browse(cr, uid, ids)
    #     pattern = "^[0-9]{10}$"
    #     for data in record:
    #         if re.match(pattern, data.phone):
    #             return True
    #         else:
    #             return False
    #     return {}
    #
    # _constraints = [(is_phone, 'Error: Invalid phone', ['phone']), ]