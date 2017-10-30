#!/usr/bin/env python
# -*- coding: utf-8 -*
from module.IMPage import IMPage

class hom(IMPage):
    def test_home(self):
        IMPage.sendMessage(self)
