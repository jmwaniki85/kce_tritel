from openerp import fields, models, api

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    items = fields.Char(compute = 'get_items')

    @api.one
    @api.depends('invoice_line')
    def get_items(self):
        items = ''
        for line in self.invoice_line:
            items += line.name +", "
        self.items = items
