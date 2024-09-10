from odoo import fields, models
from dateutil.relativedelta import relativedelta


class TestModel(models.Model):
    _name = "test.model"
    _description = "test model"
    
    

    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=fields.Date.today()+ relativedelta(months=3))
    expected_price = fields.Float(required=True,readonly=True)
    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(required=True,copy=False,default='nuevo',selection=[('nuevo','Nuevo'),('oferta recibida','Oferta recibida'),('oferta aceptada','Oferta aceptada'),('vendido','Vendido') ,('cancelado','Cancelado')])
    
    
