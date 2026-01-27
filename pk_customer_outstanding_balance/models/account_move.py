from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    outstanding_balance = fields.Monetary(
        string='Outstanding Balance',
        compute='_compute_outstanding_balance',
        store=False,  # Not stored, computed dynamically
    )

    @api.depends('partner_id', 'state', 'payment_state')
    def _compute_outstanding_balance(self):
        for move in self:
            # Only calculate if the record is saved in the database
            if move.partner_id and move.id:
                outstanding_invoices = self.env['account.move'].search([
                    ('partner_id', '=', move.partner_id.id),
                    ('state', '=', 'posted'),
                    ('payment_state', '!=', 'paid'),
                    ('move_type', '=', 'out_invoice'),
                    ('id', '!=', move.id),  # Exclude the current invoice
                ])
                move.outstanding_balance = sum(outstanding_invoices.mapped('amount_residual'))
            else:
                move.outstanding_balance = 0.0
