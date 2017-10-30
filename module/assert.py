#!/usr/bin/env python
# -*- coding: utf-8 -*
from testUtils.Driver import DesiredOptions

class assertPage(DesiredOptions):
 def asert(self):
    mylist = ['item']
    assert len(mylist) >= 1
    mylist.pop()
    assert len(mylist) >= 1