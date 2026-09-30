menu = {

    "coffee": 800,
    "tea": 120,
    "cake": 550,
    "water": 120,
    "pasta": 600
}

# Greeting

print("WELCOME TO THE COFFEE BARISTA")

print("-------- MENU -------")

print("Coffee\nTea\nCake\nWater\nPasta")

item1 = input("Order Anything From The Menu: ")

bill = 0

if item1 in menu:

    bill += menu[item1]

    print(f"You Have Added {item1}")

else:

    print(f"{item1} is not Available!")


another_order = input("Do you want to Order Another Item: [yes/no] ")

if another_order == "no" or another_order == "NO":

    print(f"Your Total Bill is {bill}")

elif another_order == "yes" or another_order == "YES":

    item_2 = input("Enter item: ")

    if item_2 in menu:

        bill += menu[item_2]

        print(f"Your {item_2} is Added!")

        print(f"Your Total Bill is {bill}")

    else:

        print(f"{item_2} is not Available!")

else:

    print("Please enter yes or no.")