"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""

from typing import Any


def foo(x: Any) -> Any:
    return x


"""
RESULT


foo(1)
foo("10")
foo(1, 2)  # expect-type-error
"""
