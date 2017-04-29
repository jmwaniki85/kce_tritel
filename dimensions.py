'''
Dimension Management refers to Reporting Levels
This will help partition transactions depending
on the reporting levels that are important to the company.
All financial documents will carry dimension data
Unlike traditional openerp extensions, all extensions
to native openerp models and views will be done from
this document and the views document under
views/dimensions.xml

Author>>Tritel Technologies

Please document all affected modules in case you customize this
document in the section below
'''

#account.move.line
#account.invoice
#account.voucher -->To accomodate payments

from openerp import models, fields, api

class dimension(models.Model):
    _name = 'dimensions'

    name = fields.Char()
    description = fields.Char()
    sequence = fields.Integer()

class dimension_values(models.Model):
    _name = 'dimension.values'

    name = fields.Char(string = 'Dimension Value')
    dimension = fields.Many2one('dimensions')
    sequence = fields.Integer()

    @api.onchange('dimension')
    def apply_dimension_sequence(self):
        self.sequence = self.env['dimensions'].search([('id','=',self.dimension.id)]).sequence

class reporting_levels(models.Model):
    _name = 'dimensions.reporting.levels'

    name = fields.Char()
    level1 = fields.Many2one('dimensions')
    level2 = fields.Many2one('dimensions')
    level3 = fields.Many2one('dimensions')
    level4 = fields.Many2one('dimensions')
    dimensions_mandatory = fields.Boolean()

    @api.onchange('level1','level2','level3','level4')
    def apply_dimension_sequence(self):
        #dimensions
        self.env['dimensions'].search([('id','=',self.level1.id)]).write({'sequence':1})
        self.env['dimensions'].search([('id','=',self.level2.id)]).write({'sequence':2})
        self.env['dimensions'].search([('id','=',self.level3.id)]).write({'sequence':3})
        self.env['dimensions'].search([('id','=',self.level4.id)]).write({'sequence':4})
        #dimension values
        self.env['dimension.values'].search([('dimension','=',self.level1.id)]).write({'sequence':1})
        self.env['dimension.values'].search([('dimension','=',self.level2.id)]).write({'sequence':2})
        self.env['dimension.values'].search([('dimension','=',self.level3.id)]).write({'sequence':3})
        self.env['dimension.values'].search([('dimension','=',self.level4.id)]).write({'sequence':4})

class account_move_line(models.Model):
    _inherit = 'account.move.line'

    dimension1 = fields.Many2one('dimension.values', domain = [('sequence','=',1)])
    dimension2 = fields.Many2one('dimension.values', domain = [('sequence','=',2)])
    dimension3 = fields.Many2one('dimension.values', domain = [('sequence','=',3)])
    dimension4 = fields.Many2one('dimension.values', domain = [('sequence','=',4)])

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    dimension1 = fields.Many2one('dimension.values', domain = [('sequence','=',1)])
    dimension2 = fields.Many2one('dimension.values', domain = [('sequence','=',2)])
    dimension3 = fields.Many2one('dimension.values', domain = [('sequence','=',3)])
    dimension4 = fields.Many2one('dimension.values', domain = [('sequence','=',4)])

    @api.multi
    def post_dimensions(self):
        self.write({})

        #handle null values
        dimension1 = None
        dimension2 = None
        dimension3 = None
        dimension4 = None

        if self.dimension1:
            dimension1 = self.dimension1.id

        if self.dimension2:
            dimension2 = self.dimension2.id

        if self.dimension3:
            dimension3 = self.dimension3.id

        if self.dimension4:
            dimension4 = self.dimension4.id

        for inv in self:

            self._cr.execute(""" UPDATE account_move_line SET dimension1=%s, dimension2=%s, dimension3=%s, dimension4=%s
                           WHERE move_id=%s """,
                        (dimension1, dimension2, dimension3, dimension4,  inv.move_id.id))

class account_voucher(models.Model):
    _inherit = 'account.voucher'

    dimension1 = fields.Many2one('dimension.values', domain = [('sequence','=',1)])
    dimension2 = fields.Many2one('dimension.values', domain = [('sequence','=',2)])
    dimension3 = fields.Many2one('dimension.values', domain = [('sequence','=',3)])
    dimension4 = fields.Many2one('dimension.values', domain = [('sequence','=',4)])

    @api.multi
    def post_dimensions(self):
       #handle null values
        dimension1 = None
        dimension2 = None
        dimension3 = None
        dimension4 = None

        if self.dimension1:
            dimension1 = self.dimension1.id

        if self.dimension2:
            dimension2 = self.dimension2.id

        if self.dimension3:
            dimension3 = self.dimension3.id

        if self.dimension4:
            dimension4 = self.dimension4.id

        for inv in self:

            self._cr.execute(""" UPDATE account_move_line SET dimension1=%s, dimension2=%s, dimension3=%s, dimension4=%s
                           WHERE move_id=%s """,
                        (dimension1, dimension2, dimension3, dimension4,  inv.move_id.id))

