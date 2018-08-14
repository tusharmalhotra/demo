from odoo import models, fields


class SchoolData(models.Model):
    _name = 'school.data'
    school_id = fields.Char('ID', required=True)
    school_name = fields.Char('Name', required=True)
    school_address = fields.Char('Address', required=True)
    school_state = fields.Char('State', required=True)
    school_city = fields.Char('City', required=True)
    school_zip = fields.Char('ZIP Code', required=True)
