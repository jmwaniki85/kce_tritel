from openerp import models, fields, api
from openerp.exceptions import ValidationError

class res_partner(models.Model):
    _inherit = 'res.partner'

    balance = fields.Float(compute = 'calculate_balance')
    invoice_ids = fields.One2many('account.invoice','partner_id')
    identification = fields.Char(string = "ID/COMPANY REGISTRATION")

    @api.one
    @api.depends('invoice_ids')
    def calculate_balance(self):
        for line in self.invoice_ids:
            self.balance += line.residual

    @api.onchange('name')
    def check_unique_name(self):
        if self.name:
            count = self.env['res.partner'].search_count([('name','=',self.name)])
            if count > 1:
                return {
                    'warning': {
                        'title': "The name exists!",
                        'message': "You cannot register a record with that name because it already exists",
                    },
                }

    @api.one
    @api.constrains('name')
    def check_unique_name_constraint(self):
        if self.name:
            count = self.env['res.partner'].search_count([('name','=',self.name)])
            if count > 1:
                raise ValidationError('You cannot register a record with that name because it already exists')
