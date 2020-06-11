# Copyright 2020 omolonlsn@gmail.com
{
    'name': 'Stock Total Cost Plus Landed Cost',
    'version': '12.0.1.0.0',
    "author": "omolonlsn@gmail",
    'license': 'AGPL-3',
    'category': 'Stock',
    'website': 'omolonlsn@gmail',
	'depends': [
        'stock',
    ],
    'data': [
        'views/stock_landed_cost_views.xml',
    ],

    'installable': True,
	'auto_install': False,
}
