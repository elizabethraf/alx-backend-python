#!/usr/bin/env python3
""" Display annotated function params"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the value """
    return [(i, len(i)) for i in lst]
