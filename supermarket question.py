#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:10:16 2026

@author: simon
"""

class Supermarket:
    def __init__(self, frozen_foods, fresh_foods, vegatables):
        self.frozen_foods = frozen_foods
        self.fresh_foods = fresh_foods
        self.vegatables = vegatables
        
    def buy_foods(self, foods, amount):
        self.foods += amount
        print(self.foods)
        