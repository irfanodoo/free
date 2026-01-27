from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_code = fields.Char(string="Price Code", help="Products with the same code will have synchronized prices.")
    e_code = fields.Char(string="Embroidery Code")
    h_code = fields.Char(string="Handmade Embroidery")

    @api.onchange('price_code')
    def _onchange_price_code(self):
        if self.price_code:
            price_code_record = self.env['price.code'].search([('price_code', '=', self.price_code)], limit=1)
            if price_code_record:
                self.list_price = price_code_record.price