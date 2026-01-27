# my_module/models/my_model.py
from odoo import models, fields, api


class PriceCode(models.Model):
    _name = 'price.code'
    _description = 'Price Code Model'
    _rec_name = 'price_code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    price_code = fields.Char(string='Price Code', required=True, tracking=True)
    price = fields.Monetary(string='Price', required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self.env.company.currency_id)

    @api.model
    def create(self, vals):
        record = super(PriceCode, self).create(vals)
        record._update_prices()
        return record

    def write(self, vals):
        res = super(PriceCode, self).write(vals)
        if 'price' in vals or 'price_code' in vals:
            self._update_prices()
        return res

    def _update_prices(self):
        for record in self:
            # Find products with the same price_code
            products = self.env['product.product'].search([('price_code', '=', record.price_code)])
            templates = self.env['product.template'].search([('price_code', '=', record.price_code)])

            # Update prices for all matching products and templates
            products.write({'list_price': record.price})
            templates.write({'list_price': record.price})


