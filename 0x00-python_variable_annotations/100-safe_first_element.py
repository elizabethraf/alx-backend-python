#!/usr/bin/env python3
from typing import Sequence, Union, Any
"""Display correct duck-typed annotations"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Define duck-typing """
    if lst:
        return lst[0]
    else:
        return None
