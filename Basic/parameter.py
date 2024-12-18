"""
TODO:

foo should accept an integer argument.
"""


def foo(x: int) -> int:
    return x


"""
RESULT


foo(10)

foo("10")  # expect-type-error
"""