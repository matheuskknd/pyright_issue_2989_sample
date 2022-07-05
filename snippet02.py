#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import Union, Any
from functools import total_ordering


@total_ordering
class FooBase:

    def __lt__(self, __o: Any) -> bool:
        return True


@total_ordering
class Foo(FooBase):

    # This IS okay
    def workingFoo_1(self, other: Union["Foo", "Bar"]) -> str:
        assert isinstance(other, (Foo, Bar))
        if isinstance(other, FooBase):
            return other.bar()
        else:
            return ""

    # This IS okay
    def workingFoo_2(self, other: Union["Foo", int]) -> str:
        assert isinstance(other, (Foo, int))
        if isinstance(other, Foo):
            return other.bar()
        else:
            return ""

    # This ISN'T okay
    def notWorkingFoo(self, other: Union["Foo", int]) -> str:
        assert isinstance(other, (Foo, int))
        if isinstance(other, FooBase):
            return other.bar()
        else:
            return ""

    def bar(self) -> str:
        return ""


@total_ordering
class Bar(FooBase):

    def bar(self) -> str:
        return ""


reveal_type(Foo)
