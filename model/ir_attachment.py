from odoo import api, fields, models, tools, _

class IrAttachment(models.Model):
	_inherit = "ir.attachment"

	@api.model
	def check(self, mode, values=None):
		res = super(IrAttachment, self.sudo()).check(mode=mode, values=values)
		return res