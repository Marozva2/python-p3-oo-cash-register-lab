#!/usr/bin/env python3
'''CashRegister'''


class CashRegister:
    '''A class representing a cash register.'''

    def __init__(self, discount: float = 0):
        '''Initialize a new CashRegister instance.'''
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title: str, price: float, quantity: int = 1):
        '''Add items to the cash register.'''
        for _ in range(quantity):
            self.items.append(title)

        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        '''Apply a discount to the total.'''
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round(self.total - (self.total * self.discount/100))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        '''Void the last transaction.'''
        self.total -= self.last_transaction
