# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from ._dunders import (
    NOTHING,
)
from ._funcs import (
    ls,
    to_dict,
    has,
)
from ._make import (
    Attribute,
    _add_methods,
    _make_attr,
)
from . import validators

__version__ = "15.0.0.dev0"
__author__ = "Hynek Schlawack"
__license__ = "MIT"
__copyright__ = "Copyright 2015 Hynek Schlawack"


attributes = s = _add_methods
attr = ib = _make_attr

__all__ = [
    "Attribute",
    "NOTHING",
    "attr",
    "attributes",
    "has",
    "ib",
    "ls",
    "s",
    "to_dict",
    "validators",
]