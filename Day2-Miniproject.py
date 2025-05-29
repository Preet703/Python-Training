inventory = {}
def addProduct():
    name = input("Enter the name of Product you want to add: ").strip()
    if name in inventory:
        print("Product already Added in inventory")
        return
    else:
        qyt = int(input("Quantity: "))
        price = int(input("Rs."))
        inventory[name] = {"quantity" : qyt, "Price" : price}

def updateProduct():
    name = input("Enter the product name you want to update: ").strip()
    if name in inventory:
        print("Choose What to update: \n 1.Quantity \n 2.Price \n 3. Both")
        choice = int(input("Choose: "))
        if(choice == 1):
            qyt = int(input("Update Quantity: "))
            inventory[name]["quantity"] = qyt
            return
        elif(choice == 2):
            price = int(input("Update Price: "))
            inventory[name]["Price"] = price
            return
        elif(choice == 3):
            qyt = int(input("Update Quantity: "))
            price = int(input("Update Price: "))
            inventory[name] = {"quantity" : qyt, "Price" : price}
            return
        else:
            return "Wrong input {choice}. Try again"
    
def deletProduct():
    name = input("Enter the name of Product you want to delet: ").strip()
    if name in inventory:
        del inventory[name]
        return

def viewInventory():
    for key in inventory:
        print(f"Name: {key} \n Quantity: {inventory[key]['quantity']}, Price: {inventory[key]['Price']}")

while True:
    print('''
          Choose what you want to do:
          1. Add Product
          2. Update Product
          3. Delet Product
          4. View Inventory
          5. Exit
''')
    choose = int(input("Choose: "))
    if choose == 1:
        addProduct()
    elif choose == 2:
        updateProduct()
    elif choose == 3:
        deletProduct()
    elif choose == 4:
        viewInventory()
    elif choose == 5:
        print("-------------------")
        break
    else:
        print("Wrong Selection! Try Again")