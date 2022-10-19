#!/usr/bin/python3
"""Locked Class."""


class LockedClass:
    """No attributes can be added."""

    def __setattr__(self, name, value):
        """Check if attribute to be set is valid."""
        if name != "first_name":
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    self.__class__.__name__, name
                )
            )
        self.__dict__[name] = value

    def __getattribute__(self, name):
        """Check if attribute to be set is valid."""
        if name == "dict":
            raise AttributeError(
                "'{}' object has no attribute '__dict__'".format(
                    self.__class__.__name__
                )
            )
        return self.__dict__[name]
