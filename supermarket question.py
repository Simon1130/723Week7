#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:10:16 2026

@author: simon
"""

class Supermarket:
#each food item in the class should be dictionary, currency is integer
#key pair is the name
#value pair is the list of amount and price
    def __init__(self, frozen_foods, fresh_foods, vegatables, currency):
        self.frozen_foods = frozen_foods
        self.fresh_foods = fresh_foods
        self.vegatables = vegatables
        self.currency = currency

#Index 0 should be amount, 1 should be price
    def buy_in_stock(self, foods, amount):
        self.foods[0] += amount
        self.currency - self.foods[1] * amount
        print(self.foods)
        
    def selling_foods(self, foods, amount):
        self.foods[0] -= amount
        self.currency + self.foods * amount
        print(self.foods)
    
    def check_currency(self):
        print(self.currency)