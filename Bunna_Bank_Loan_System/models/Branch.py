from odoo import models, fields

class Branch(models.Model):
    _name = 'bunna.branch'
    _description = 'Branch Loan Requests'

    pending_request_id = fields.Char(string='Pending Request ID', required=True)
    # employee_id = fields.Many2one('bunna.employees', string='Employee', required=True, ondelete='cascade')
    loan_amount = fields.Float(string='Loan Amount', required=True)
    # guarantee_id = fields.Many2one('bunna.guarantees', string='Guarantee', required=True, ondelete='set null')
    repayment_period = fields.Integer(string='Repayment Period (Months)', required=True)
    loan_status = fields.Selection([
        ('pending', 'Pending'),
        ('granted', 'Granted')
    ], string='Loan Status', default='pending', required=True)
    branch_id = fields.Char(string='Branch ID', required=True)
    district_name = fields.Char(string='District Name', required=True)
