#!/usr/bin/python3
"""
Definition of a locked class.
"""


class LockedClass:
    """LockedClass is a class that restricts attribute assignment to
    'first_name'."""

    __slots__ = ('first_name',)
