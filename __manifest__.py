# __manifest__.py
# -*- coding: utf-8 -*-
{
    'name': "DTN PoS Disable Screensaver",
    'summary': "Вимкнення заставки та скринсейвера (SaverScreen) у Точці продажу",
    'description': """
        Модуль для Odoo 18.0 Community Edition.
        Нейтралізує idleTimeout сервісу PosStore, запобігаючи переходу інтерфейсу 
        касира та екрана блокування в режим скринсейвера SaverScreen під час простою.
    """,
    'author': "Drauthran",
    'website': "https://github.com/drauthran",
    'category': 'Sales/Point of Sale',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'dtn_pos_disable_screensaver/static/src/app/store/pos_store.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}