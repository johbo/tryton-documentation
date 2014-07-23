#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .library import Book


def register():
    #Pool.register(
    #   module='library', type_='report')
    Pool.register(
        Book,
        module='library', type_='model'
    )


