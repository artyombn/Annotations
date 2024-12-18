"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""
from typing import ClassVar, Any


class Foo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int] = 1


"""
RESULT


Foo.bar = 1
Foo.bar = "1"  # expect-type-error
Foo().bar = 1  # expect-type-error
"""