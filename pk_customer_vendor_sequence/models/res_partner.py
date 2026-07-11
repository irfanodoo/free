from odoo import models, fields, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    sequence_number = fields.Char(string='Number', copy=False, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        # vals_list is always a list of dictionaries
        for vals in vals_list:
            # Check context to determine which sequence to use
            if self.env.context.get('default_customer_rank', 0) > 0:
                vals['sequence_number'] = self.env['ir.sequence'].next_by_code('res.partner.customer.sequence')

            elif self.env.context.get('default_supplier_rank', 0) > 0:
                vals['sequence_number'] = self.env['ir.sequence'].next_by_code('res.partner.vendor.sequence')

        # Pass the processed vals_list to the super method
        return super(InheritResPartner, self).create(vals_list)