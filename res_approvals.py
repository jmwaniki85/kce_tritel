'''
#	create approval tables to be used system-wide
#	approval templates
#	approval entry
#	additional approvers
#
#
#
#	Design by Tritel Technologies:::>>>dennokorir
#	Simple but effective design
#	All tables are designed here. All the approval functions will be inside the openerp folder in approvals.py
#	This is to make it extensible to other modules
'''
from openerp import fields,models,api

class approval_template(models.Model):
	_name = 'approval.template'


	name = fields.Char(string = 'Approval Code')
	description = fields.Char()
	document_type = fields.Selection([('member_app',"Member Application"),('closure',"Member Closure"),('loan',"Loan")])
	limit_type = fields.Selection([('checker',"Checker"),('tiered',"Tiered")])
	additional_approvers = fields.Boolean(compute = 'sum_additional_approvers', readonly = True)
	enabled = fields.Boolean()
	department = fields.Char()
	no_of_approvers = fields.Integer(compute = 'sum_additional_approvers', readonly = True)
	additional_approver_ids = fields.One2many('additional.approvers','template_id')

	@api.one
	@api.depends('additional_approver_ids')
	def sum_additional_approvers(self):
		self.no_of_approvers = self.env['additional.approvers'].search_count([('template_id','=',str(self.id))])#len(self.additional_approver_ids)
		if self.no_of_approvers > 0:#len(self.additional_approver_ids)>0:
			self.additional_approvers = True

class approval_entry(models.Model):
	_name = 'approval.entry'

	document_type = fields.Selection([('member_app',"Member Application"),('closure',"Member Closure"),('loan',"Loan")])
	document_no = fields.Char()
	document_id = fields.Char()#this field will be a link betweeen the document and approval entries

	sequence = fields.Integer()
	sender_id = fields.Char()
	approver_id = fields.Char()
	sender = fields.Many2one('res.users')
	approver = fields.Many2one('res.users')
	status = fields.Selection([('created',"Created"),('open',"Open"),('cancelled',"Cancelled"),('rejected',"Rejected"),('approved',"Approved")])

class additional_approvers(models.Model):
	_name = 'additional.approvers'

	approver_id = fields.Many2one('res.users')
	minimum_amount = fields.Float()
	maximum_amount = fields.Float()
	template_id = fields.Many2one('approval.template')
