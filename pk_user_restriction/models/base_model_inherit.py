# models/base_model_inherit.py

from odoo import models, _, api
from odoo.exceptions import UserError

class BaseModel(models.AbstractModel):
    _inherit = 'base'

    def unlink(self):
        # Check if the current user is in 'No Delete Group'
        if self.env.user.has_group('pk_user_restriction.group_no_delete'):
            raise UserError(_("You are not allowed to delete records."))
        return super(BaseModel, self).unlink()

    def write(self, vals):
            # Check if the current user is in 'No Update Group'
            if self.env.user.has_group('pk_user_restriction.group_no_update'):
                raise UserError(_("You are not allowed to update records."))
            return super(BaseModel, self).write(vals)
    @api.model_create_multi
    def create(self, vals):
                # Check if the current user is in 'No Create Group'
                if self.env.user.has_group('pk_user_restriction.group_no_create'):
                    raise UserError(_("You are not allowed to create records."))
                return super(BaseModel, self).create(vals)
