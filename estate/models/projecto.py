from odoo import fields, models


class TestModel(models.Model):
    _name = "test.model"
    _description = "test model"
    
    

    name = fields.Char(required=True)
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
   # garden_orientation = fields.Selection(selection=[('North'), ('South'), ('East'), ('West')])
