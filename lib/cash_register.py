#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize a CashRegister with optional discount
        
        Args:
            discount (int, optional): Percentage discount to apply to total. Defaults to 0.
        """
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the discount value"""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount value
        Validates that discount is an integer between 0-100
        
        Args:
            value: The discount percentage
        """
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self._discount = value
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register
        
        Args:
            item (str): Name of the item
            price (float): Price of the item
            quantity (int, optional): Quantity of the item. Defaults to 1.
        """
        # Add price to total
        self.total += price * quantity
        
        # Add items to the items array
        self.items.extend([item] * quantity)
        
        # Add transaction to previous_transactions
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
    
    def apply_discount(self):
        """
        Apply the current discount to the total
        
        If no discount is set, prints an error message
        Otherwise, applies the discount and prints the new total
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate the discounted total
            self.total = self.total * (1 - self.discount / 100)
            # Format the total to remove trailing decimal if it's a whole number
            formatted_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction from the register
        
        Updates the total and items list to reflect the removal
        """
        if not self.previous_transactions:
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract from total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        
        # Ensure total doesn't go below 0
        if self.total < 0:
            self.total = 0.0
        
        # Remove items from items list
        item_to_remove = last_transaction["item"]
        quantity_to_remove = last_transaction["quantity"]
        
        # Remove items from the end of the list
        for _ in range(quantity_to_remove):
            if item_to_remove in self.items:
                self.items.remove(item_to_remove)