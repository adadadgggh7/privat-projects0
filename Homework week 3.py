#1 Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a python app which will ask day number, and return the day name (a string)

# our_number = int(input("day number "))
# if our_number == 0:
#   print('Monday')
# if our_number == 1:
#   print('Tuesday') 
# if our_number == 2:
#   print('Wednesday')
# if our_number == 3:
#   print('Thursday')
# if our_number == 4: 
#   print('Friday')
# if our_number == 5: 
#   print('Saturday')
# if our_number == 6: 
#   print('Sunday')

#2 Write a python program which takes string as input then checks if there is a space in string ( it means that users inputed the word or the sentence ) then print message for both cases

# our_word_or_sentence = input('what you wanna say ')
# if ' ' in our_word_or_sentence : 
#     print('thats sentence')
# else:
#     print('thats word')

#3 Write a Python program to add ‘ing’ at the end of a given string (length should be at least 3). If the given string already ends with ‘ing’ then add ‘ly’ instead. If the string length of the given string is less than 3, leave it unchanged. Sample String : ‘abc’ Expected Result : ‘abcing’ Sample String : ‘string’ Expected Result : ‘stringly’ (“abs”.endswith(“ing”) -> false)

# text_exe = input('our word ')
# if len(text_exe) < 3:
#     print('small length')
# elif text_exe.endswith('ing'):
#     print(text_exe + 'ly')
# else:
#     print(text_exe +'ing')

#4 Write a python program which takes from user three numbers and returns the maximum of them. 

# first_numb = int(input('first number '))
# second_numb = int(input('second number '))
# third_numb = int(input('third number '))
# if first_numb > second_numb and first_numb > third_numb:
#      print('first numb max')
# if second_numb > first_numb and second_numb > third_numb:
#      print('second number max')
# if third_numb > first_numb and third_numb > second_numb:
#     print('third number max')



#foodcourt now with if and else and other things 

# Kebab_price = 2000
# Pizza_price = 1000
# Mayo_price = 500
# Ketchup_price = 100 
# print('\t==Hello for our food court=='
#     '\nthis is our menu',
#     '\nKhebab => ',Kebab_price,'֏'
#     '\nPizza =>',Pizza_price,'֏')
# order = input('what you wanna eat ')
# order_name = ""
# order_price = 0
# if order == 'Pizza' or order == 'pizza' or order == 'p' or order == 'pi' or order == 'piz':
#     order_price = Pizza_price
#     order_name = 'Pizza'
#     print('\tOh Pizza \ngood choice')
        
# elif order == 'Kebab' or order == 'kebab' or order == 'keb' or order == 'K'or order == 'k'or order == 'ke' or order == 'keb':
#     order_price = Kebab_price
#     print('\tKebab!!! \ndude our kebabs are best in whole town')
#     order_name = 'Kebab'
# else:
#    order_price = 0
#    print("sorry we didnt have that")
#    order_name = ''
# print("Want souse (?) ==> ",'Ketchup > ',Ketchup_price,'֏''/ Mayones > ',Mayo_price,'֏ or Nothing ?')
# sec_order = input()
# if sec_order == 'Ketchup' or sec_order == 'K' or sec_order == 'Ket' or sec_order == 'ketchup' or sec_order == 'k' or sec_order == 'ke' or sec_order == 'ket':
#     print('all right')
#     sec_prorder = Ketchup_price
#     sec_order_name = "Ketchup"
# if sec_order == 'Mayo' or sec_order == 'Ma' or sec_order == 'May' or  sec_order == 'mayo' or sec_order == 'm' or sec_order == 'ma' or sec_order == 'may':
#     print('all right')
#     sec_prorder = Mayo_price  
#     sec_order_name = "Mayones" 
# elif sec_order == '' or sec_order == 'n' or sec_order == 'not' or sec_order == 'N' or sec_order == 'Not' or sec_order == 'nty':
#     sec_prorder = 0
#     print("well nothing so nothing")
# your_money = int(input('How much money you have '))
# This = print('\t''With',str(your_money) + ('֏'))
# print('********************************************')
# print('\n'"\tYou order is \t Price")
# if order_price + sec_prorder == 0:
#     print(" No valid food selected")
# elif your_money >= sec_prorder + order_price:
#     if order_price == 0 or sec_prorder == 0:
#         print(order_name,sec_order_name,'=====>',sec_prorder + order_price,'֏')
#     else:
#         print(order_name,'with',sec_order_name,'=====>',sec_prorder + order_price,'֏')

# else:
#     if your_money < sec_prorder + order_price:
#         print('Sorry,you don’t have enough money for that order')