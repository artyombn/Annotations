"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar

# For Python < 3.12
# F = TypeVar("F", bound=Callable[..., None])

# For Python >= 3.12
def decorator[T: Callable](func: T) -> T:
    return func