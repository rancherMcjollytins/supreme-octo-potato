firstName = None
lastName = None
orderedItems = []
totalval = 0
finalprice = 0

orderableItems = {
    "Pie" : 5.00,
    "Sausage Roll" : 3.50,
    "Juice" : 2.50,
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
    return firstName, lastName

def orderItems(cart, total):
    print("|-------| Menu |-------|")
    #this for loop was originally for i in orderableitems: print(f"{i} : {orderableItems([i])}"")
    #i changed it to this with the enumnerate based on oscar dodd code
    for i, item in enumerate(orderableItems):
        print(f"{i + 1} : {item} - ${orderableItems[item]}")
    print("|----------------------|")
    while True:
        orderedItem = None
        orderedItem = input("Order Here! (input next to finish order.): ")
        if orderedItem.title() in orderableItems:
            print(f"Added {orderedItem} to cart!")
            cart.append(orderedItem)
            for cartitem in cart:
                print(f"- {cartitem}")
                #this was originally cartitem.capitalize, but due to errors with sausage roll, juice bomb and
                #other items with multiple words, i had to change it. I searched up capitalize and google (ai)
                #told me about the title method.
                #also I put the total math line in the forloop and the problem was for every item ordered
                #it increased the total by the (total + newitem) instead of just by the item, im too tired
                #to figure out the logic in this right now so yeah it makes sense though with how addition
                #and increments work.
            total += orderableItems[cartitem.title()]
            print("|-------| Total |-------|")
            print(f"Total: ${total}")
        elif orderedItem.lower() == "next":
            break
    return total

def discountApplier(totalprice, discountedprice):
    if totalprice >= 20:
        discountedprice = totalprice * 0.9
        print(f"Order is over/equal to $20. Discount applied.")
    else:
        discountedprice = totalprice
        print(f"Order is not over $20. Discount not applied.")
    return discountedprice
            


addUsername()
print(f"Hello! {firstName} {lastName}")
print()
totalval = orderItems(orderedItems, 0)
print()

finalprice = discountApplier(totalval, 0)
print()
print(f"Thank you for ordering, {firstName} {lastName}.")
print("|-------| Cart |-------|")
for i in orderedItems:
    print(f"- {i}")
print("|-------| Total |-------|")
print(f"Total: ${finalprice}")