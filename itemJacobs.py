"""
File: itemJacobs.py
This module defines the Item class
"""
class Item:
    
    def __init__(self,name = "item",quantity = 1,price = 1.0):
        """Initializes a basic Item Object with default parameters."""
        self.thisName = name
        self.thisQuantity = quantity
        self.thisPrice = price

    def getName(self):
        """Returns the name of the Item."""
        return self.thisName
    
    def setName(self,newName):
        """Sets a new name to the Item."""
        self.thisName = newName
    
    def getQuantity(self):
        """Returns the quantity of the Item."""
        return self.thisQuantity
    
    def setQuantity(self,newQuantity):
        """Sets a new quantity to the Item."""
        self.thisQuantity = newQuantity
    
    def getPrice(self):
        """Returns the price of the Item."""
        return self.thisPrice
    
    def setPrice(self,newPrice):
        """Sets a new price of the Item."""
        self.thisPrice = newPrice
    
    def __str__(self):
        """Returns a detailed description of an Item."""
        result = "Name: "+self.thisName
        result += "\nQuantity: "+str(self.thisQuantity)
        result += "\nPrice: ${0:0.2f}".format(self.thisPrice)
        return result


