##
## Name: Luke Jacobs
## Prog9Jacobs.py
##
## Purpose: This Program acts as an grocery shopping simulator in which
##          users can select different goods to buy from a store.
##
## File Input: A file is first inputted with several items.
##        
## Input: The user will then choose different tasks from a menu by inputting
##        a number between 0-9.
##
## Output: Based on wihchever part of the program the user decides to choose.
##
## Certification of Authenticity: I certify that this lab is entirely
##         my own work.
##

#Imports Item from itemJacobs
from itemJacobs import Item
def main():
    
    #Greet the user :)
    print("Welcome to Luke's Grocery Store!")

    #Gets the file directory and opens the file
    fileName = input("Enter the name of the file: ")
    file = open(fileName,"r")

    #Instantiates list that will hold the Item objects
    itemList = []
    
    #Gets the number of items
    numOfItems = int(file.readline())

    #Loops through however many of items
    #Creates an item for the given data
    for item in range(numOfItems):
        name = file.readline().strip()
        quantity = int(file.readline())
        price = float(file.readline())
        newItem = Item(name,quantity,price)
        itemList.append(newItem)
        
    #User menu for the user to navigate the program
    menu = "1. Add an item to the list\n" \
           "2. Delete an item from the list\n" \
           "3. Print each item in the list\n" \
           "4. Search for a user-specified item in the list\n" \
           "5. Count the total number of items in the list\n" \
           "6. Total the cost of the items in the list\n" \
           "7. Determine whether the list is empty\n" \
           "8. Clear the list\n" \
           "0. Quit\n" \
           "Enter a number: "

    number = "19"

    #Checks to see if the user has inputted zero.
    while number != "0":
        number = input("Enter a number for a menu option: ")
        #Validates the input data from the user
        while number != "1" and number != "2" and number != "3" \
              and number != "4" and number != "5" and number != "6" \
              and number != "7" and number != "8" and number != "0":
            number = input("Enter a correct option: ")

        #Depending on the number inputted, a specific function is called
        if number == "1":
            addItem(itemList)
        elif number == "2":
            name = input("Enter the name of the item you would like to delete: ")
            deleteItem(itemList,name)
        elif number == "3":
            printList(itemList)
        elif number == "4":
            name = input("Please enter the name of the item to find in your cart: ")
            print(searchItem(itemList,name))
        elif number == "5":
            count = countList(itemList)
            print("Your cart contains a total of "+str(count)+" items.")
        elif number == "6":
            total = totalCost(itemList)
            print("The total price of all your items is ${0:0.2f}".format(total))
        elif number == "7":
            empty = isListEmpty(itemList)
            if empty == True:
                print("Your cart is empty.")
            else:
                print("Your cart is not empty.")
        elif number == "8":
            clearList(itemList)
            print("The list has been cleared.")
        elif number == "0":
            print("Thanks for using this program")   
    
# addItem
#
# Creates a new item, then adds it to the list
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns None
def addItem(aList):
    print("Please provide information about the item to add.")
    name = input("Please enter the name: ")
    quantity = int(input("Please enter the quantity: "))
    while quantity < 1:
        quantity = int(input("Please enter a correct quantity:" ))
    unitPrice = float(input("Please enter the price: "))
    while unitPrice <= 0:
        unitPrice = float(input("Please enter a correct unit price: "))
    newItem = Item(name,quantity,unitPrice)
    aList.append(newItem)
    
# deleteItem
#
# Deletes an item from the list
#
# Parameters:
#   - aList: a list of items
#   - itemName: a name of an item
#
# Returns: returns None
def deleteItem(aList, itemName):
    isDeleted = False
    for i in range(len(aList)):
        
        if (len(aList)-i > 0) and aList[i].getName() == itemName:
            del aList[i]
            i-= 1
            isDeleted = True
            
            
    if isDeleted == False:
        print("Sorry, but your cart does not contain the item "+itemName)

# printList
#
# Prints the entirety of a list of items
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns None
def printList(aList):
    for i in range(len(aList)):
        print("---Item Number "+str(i+1)+"---")
        print(aList[i])
        print()

# searchItem
#
# Searches for an item in an array of items
#
# Parameters:
#   - aList: a list of items
#   - itemName: a name of an item
#
# Returns: returns a String of the search result
def searchItem(aList,itemName):
    result = ""
    for item in aList:
        name = item.getName()
        if name == itemName:
            result = "Yes, you have "+str(item.getQuantity())
            if item.getQuantity() > 1 and name[-1] != "s":
                result += " "+itemName+"s at ${0:0.2f} each.".format(item.getPrice())
            else:
                result += " "+itemName+" at ${0:0.2f} each.".format(item.getPrice())
    return result

# countList
#
# Finds how many items are in a list of items
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns how many items are in the list of items
def countList(aList):
    count = 0
    for item in aList:
        count+= 1
    return count

# totalCost
#
# Finds the total cost of all the items in a list
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns the total price from a list of items
def totalCost(aList):
    total = 0.0
    for item in aList:
        total += (item.getPrice()*item.getQuantity())
    return total

# isListEmpty
#
# Determines whether a list is empty or not
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns a boolean
def isListEmpty(aList):
    isEmpty = False
    if len(aList) == 0:
        isEmpty = True
    return isEmpty

# clearList
#
# Clears the whole list
#
# Parameters:
#   - aList: a list of items
#
# Returns: returns None
def clearList(aList):
    for i in range(len(aList)-1,-1,-1):
        del aList[i]

#Call main
main()
