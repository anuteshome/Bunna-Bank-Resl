from odoo import models,fields

class Hr(models.Model):
    _name = 'bunna.hr'
    _description = 'hr Employee'

    branch_id = fields.Char(string='Branch ID')
    district_name = fields.Char(string="District Name")
    branch_name = fields.Char(string="Branch Name")
    number_of_employee = fields.Integer(string="Number of Employee")
    total_amount_granted = fields.Float(string="Total Amount Granted")
