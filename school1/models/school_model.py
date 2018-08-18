from odoo import models, fields


class SchoolData(models.Model):
    _name = 'school.data'

    school_id = fields.Char('ID',)
    # _sql_constraints = [
    #     ('school_id',
    #      'UNIQUE (school_id)',
    #      'School ID must be unique!')]

    name = fields.Char('School Name',)
    school_address = fields.Char('Address',)
    school_state = fields.Char('State',)
    school_city = fields.Char('City', )
    school_zip = fields.Char('ZIP Code',)
    school_class = fields.Many2many('class.data')
