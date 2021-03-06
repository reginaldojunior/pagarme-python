# -*- coding: utf-8 -*-

__version__ = '2.0.0'
__description__ = 'Pagar.me Python'
__long_description__ = 'Python library for the pagar.me gateway'

__author__ = 'Allisson Azevedo, Marcus Bodock, Igor P. Leroy'
__author_email__ = 'allisson@gmail.com, mbodock@gmail.com, ip.leroy@gmail.com'

from .card import Card
from .customer import Customer
from .pagarme_facade import PagarmeFacade as Pagarme
from .subscription import Plan, Subscription
from .transaction import Transaction

from .exceptions import *
