# -*- coding: utf-8 -*-
{
    'name': "Webservice example module",

    'summary': """Manage trainings""",

    'description': """
    Module for webservice example
    """,

    'author': "Telematel",
    'website': "http://www.telematel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/webservice_views.xml',
    ],
}
