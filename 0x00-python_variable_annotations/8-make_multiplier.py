#!/usr/bin/env python3
from typing import Callable
"""display annotated funtinon"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return Multiplier function"""
    return (lambda x: multiplier*x)
