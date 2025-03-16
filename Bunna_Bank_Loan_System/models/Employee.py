from odoo import models, fields, api
from datetime import date

class Employees(models.Model):
    _name = 'bunna.employees' 
    _inherit = ['mail.thread', 'mail.activity.mixin'] 
    _description = "Employee Table"  

    employee_id = fields.Char(string="Employee ID", required=True, index=True) 
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    salary = fields.Float(string="Salary")
    working_unit = fields.Char(string="Working Unit")
    district = fields.Char(string="District")
    date_of_birth = fields.Date(string="Date of Birth")
    date_of_employment = fields.Date(string="Date of Employment", required=True)  
    email = fields.Char(string="Email")
    phone_number = fields.Char(string="Phone Number")
    existing_loans = fields.Float(string="Existing Loans")
    isPermanent = fields.Boolean(string="Is Permanent")
    working_months = fields.Integer(string="Working Months", compute="_compute_working_months", store=True)

    @api.depends('date_of_employment')
    def _compute_working_months(self):
        for record in self:
            if record.date_of_employment:
                today = date.today()
                delta = (today.year - record.date_of_employment.year) * 12 + (today.month - record.date_of_employment.month)
                record.working_months = max(delta, 0) 
            else:
                record.working_months = 0





    # employee_id=fields.char(string="Employee ID")
    # name=fields.char(string="Name")
    # age=fields.Integer(string="Age")
    # salary=fields.Float(string="Salary")
    # working_unit=fields.char(string="Working Unit")
    # district=fields.char(string="District")
    # date_of_birth=fields.date(string="Date of Birth")
    # email=fields.char(string="Email")
    # phone_number=fields.char(string="Phone Number")
    # existing_loans=fields.Float(string="Existing Loans")
    # isPermanent=fields.Boolean(string="Is Permanent")
    # working_months=fields.Intiger(string="Working Months")
