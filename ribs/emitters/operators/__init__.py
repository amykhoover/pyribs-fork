"""Various operators which are employed across emitters.

Operators take in one or more parent solutions and output new solutions via
operators such as mutation and crossover.

.. autosummary::
    :toctree:

    ribs.emitters.operators.OperatorBase
"""
from ribs.emitters.operators._operator_base import OperatorBase

__all__ = ["OperatorBase"]

_NAME_TO_OP_MAP = {}


def _get_op(operator):
    """Retrieves Matching Operator"""
    if isinstance(operator, str):
        if operator in _NAME_TO_OP_MAP:
            operator = _NAME_TO_OP_MAP[operator]
            return operator
        else:
            raise ValueError(f"`{operator}` is not the full or abbreviated "
                             "name of a valid operator")

    raise ValueError(f"`{operator}` is not a string")
