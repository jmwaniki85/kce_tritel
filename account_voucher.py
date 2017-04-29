from openerp import fields, models, api

class account_voucher(models.Model):
    _inherit = 'account.voucher'

    def print_receipt(self):

        return self.env['report'].get_action(self, 'tritel.madiba_customer_receipt')
