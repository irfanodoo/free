from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_fixed = fields.Monetary(
        string="Discount (Fixed)",
        digits='Product Price',
        help="Fixed amount discount per line."
    )

    # 1. Fixed Amount -> Updates Percentage
    @api.onchange('discount_fixed', 'price_unit')
    def _onchange_discount_fixed(self):
        for line in self:
            if line.price_unit and line.discount_fixed:
                line.discount = (line.discount_fixed / line.price_unit) * 100
            elif line.discount_fixed == 0:
                line.discount = 0

    # 2. Percentage -> Updates Fixed Amount
    @api.onchange('discount')
    def _onchange_discount_percent(self):
        for line in self:
            if line.price_unit and line.discount:
                line.discount_fixed = (line.discount / 100) * line.price_unit

    # 3. Pass value to Invoice
    def _prepare_invoice_line(self, **optional_values):
        # Call super to get the standard dictionary
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        # Add our fixed discount to the dictionary
        res['discount_fixed'] = self.discount_fixed
        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_fixed = fields.Monetary(
        string="Discount (Fixed)",
        digits='Product Price',
        currency_field='currency_id'
    )

    # 4. INVOICE LOGIC: Fixed Amount -> Updates Percentage
    @api.onchange('discount_fixed', 'price_unit')
    def _onchange_discount_fixed(self):
        for line in self:
            if line.price_unit and line.discount_fixed:
                line.discount = (line.discount_fixed / line.price_unit) * 100

    # 5. INVOICE LOGIC: Percentage -> Updates Fixed Amount
    # (This was missing in your code! It ensures consistency if Odoo recalculates)
    @api.onchange('discount')
    def _onchange_discount_percent(self):
        for line in self:
            if line.price_unit and line.discount:
                line.discount_fixed = (line.discount / 100) * line.price_unit