# -*- coding: utf-8 -*-
{
    'name': "my-addons",

    'summary': """
    Customizations

""",

    'description': """
    This is a list of my customization:\n
    1-Adding a custom field "Available Quantity" to product template model and show it in form view.\n
    2-Customization in tree view by Adding a custom field "Available Quantity".\n
    3-Create a custom menu , action and use domain to filter records\n
    4-Create a new model and add to it menu , action and using a notebook to display related model\n
    5-Create computed field "Total Serving"\n
    6-Create kanban view \n
    7-using view inheritance to add a page to the-product notebook\n
    8-using ir.model.access.csv to configure model security\n
    9-using onchange decorator\n
    10-Creating custom report\n
    11-Using Odoo API\n
    
    """,

    'author': "Mona",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}