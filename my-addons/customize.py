from openerp import models ,fields,api
class school_product_template (models.Model):
	_name ='product.template'
	_inherit ='product.template'
	available_quantity =fields.Boolean("Available Quantity")
	@api.onchange('sale_ok')
	def check_item(self):
		if self.sale_ok == True:
			self.available_quantity=True
		else:
			self.available_quantity=False

	meal= fields.One2many('res.users.meals','product')
class custom_res_user_meal(models.Model):
	_name="res.users.meals"
	name = fields.Char('Meal Name')
	user_id =fields.Many2one('res.users','Student')
	notes = fields.Text('Meal Note')
	meal_date = fields.Datetime('Meal Date')
	product=fields.Many2one('product.template')
	item_ids = fields.One2many('res.users.mealitem','meal_id')
	@api.one
	@api.depends('item_ids.serving')
	def calcserving(self):
		currentserving=0
		for item in self.item_ids:
			currentserving =currentserving+item.serving
		self.total_serving = currentserving


	total_serving =fields.Integer(string='Total Serving',store=True,compute='calcserving')

class custom_res_user_meal_item(models.Model):
	_name="res.users.mealitem"
	meal_id =fields.Many2one('res.users.meals')
	item_id =fields.Many2one('product.template')
	notes = fields.Text('Meal Item Note')
	serving = fields.Float('Serving')
	available_quantity =fields.Boolean(related='item_id.available_quantity',string='Available Quantity',store=True,readonly=True)