
from abc import ABC, abstractmethod

class Product: 
    @abstractmethod
    def __init__(self,name, price):
        self.name = name
        self.price = price
    

    def calculate_price(self):
        pass
         

class PricingStrategy:
    @abstractmethod
    def apply(self):
        pass


class DiscountStrategy(PricingStrategy):
    def __init__(self, discount):
        self.discount = discount * 0.9
        
    def apply(self):
        return self.discount
    
    
class TaxStrategy(PricingStrategy):
    def __init__(self, tax):
        self.tax = tax * 1.2
    
    def apply(self, base_price):
        return self.tax
    
    










        