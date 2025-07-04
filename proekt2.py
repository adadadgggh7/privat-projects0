# home work 3.1 
# create an app which will exchange the given amount of money to dollar, dollar rate should be taken from another file

# dolar = 387.72


#work 3.2 
# Ask user his height and tell him the optimal weight depending of his height.  Google will help you, how to calculate this.

# height = int(input("Your height => "))
# weight = 24.9 * (0.01 * height)**2
# print("your optimal weight need to be --->",int(weight))

# #work 3.3 
# Write python program for food court. There should be a menu with two dishes, pizza and kebab, and two additions ketchup,  “Mayonez” all should have their prices. Depending on the answers of the user  the value of the price row should be True .
# EX.  pizza = 1000 , ketchup = 100, Mayonez = 500  User ordered pizza with ketchup,  then in terminal should be seen
# You have ordered pizza with Mayonez and your price is 1500 => False
# You have ordered pizza with Ketchup and your price is 1100 => True

foodcourt 

Kebab_price = 2000
Pizza_price = 1000
Mayo_price = 500
Ketchup_price = 100 
print('\t==Hello for our food court=='
	'\nthis is our menu',
	'\nKhebab => ',Kebab_price,'֏'
	'\nPizza =>',Pizza_price,'֏')
print("Want souse (?) ==> ",'Ketchup > ',Ketchup_price,'֏''/ Mayones > ',Mayo_price,'֏')
your_money = int(input('What you can order --> '))
This = print('\t''With',str(your_money) + ('֏'))