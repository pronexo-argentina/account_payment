from odoo import models, api

class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        # check: se agrega este registro para el módulo account_withholding
        res['withholding'] = {'mode': 'multi', 'domain': [('type', 'in', ['cash', 'bank'])]}
        return res
