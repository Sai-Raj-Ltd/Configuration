# Copyright 2020 omolonlsn@gmail.com
# License 
from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class AdjustmentLines(models.Model):
    _inherit = 'stock.valuation.adjustment.lines'
    
    @api.multi
    @api.depends('former_cost', 'additional_landed_cost')
    def _compute_prod_cost_total(self):
        for record in self:
            record.product_total_cost = record.former_cost + record.additional_landed_cost
            
    
    product_total_cost = fields.Float(
        string='Total Cost', 
        store=True,
        compute='_compute_prod_cost_total', 
        digits=dp.get_precision('Product Price'),
    )
    

     


   