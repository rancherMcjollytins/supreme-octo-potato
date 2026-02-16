firstName = None
lastName = None
orderedItems = ()

orderableItems = {
    "Pie" : 5.00,
    "Sausage Roll" : 3.50,
    "Juice Bomb" : 2.50,
    "Milk" : 2.00,
    "Chocolate Milk" : 2.50
}

def addUsername():
    # i tried to do a thing with a return and some parameters and other funky stuff to return the name that was inputted but it always 
    # came out as null so i had to do this
    # why????? i know the local variables wouldnt work probably but like i thought that parameters would work or maybe return or maybe
    #i had to implement it different.
    while True:
        global firstName
        global lastName
        firstName = input("Please input your first name: ")
        lastName = input("Please input your last name: ")
        correctname = input(f"Is your name {firstName.capitalize()} {lastName.capitalize()}? (yes/no): ")
        if correctname.lower() == "yes":
            break
        elif correctname.lower() == "no":
            print("Please reinput name.")
            print()
        else:
            print("An error occurred! Please retry.")

def orderItems(orderedItem):
    global orderedItems
    print("|-------| Menu |-------|")
    #this for loop was originally for i in orderableitems: print(f"{i} : {orderableItems([i])}"")
    #i changed it to this with the enumnerate based on oscar dodd code
    for i, item in enumerate(orderableItems):
        print(f"{i + 1} : {item} ${orderableItems[item]}")
    print("|----------------------|")
    while True:
        orderedItem = input("order: ")
        
        for index,order in orderedItems:
            print(index)





            


addUsername()
print(f"{firstName} {lastName}")
print()
orderItems(None)