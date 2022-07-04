#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import TypeAlias, Union
from functools import total_ordering


class Interface:
    pass


InterfaceOrInt: TypeAlias = Union[Interface, int]


@total_ordering
class FooDict(Interface, dict[int, InterfaceOrInt]):

    def foo(self) -> None:
        bar: InterfaceOrInt = self[0]
        if isinstance(bar, (FooDict, FooList)):
            _ = bar.sorted()

    def sorted(self) -> "FooDict":
        return FooDict()

    def __lt__(self, __o: object) -> bool:
        return True


@total_ordering
class FooList(Interface, list[InterfaceOrInt]):

    def sorted(self) -> "FooList":
        return FooList()


reveal_type(FooDict)
