#1 Write a program (using functions!) that asks the user for a long string containing multiple
#words. Return back to the user the same string,
#except with the words in backwards order,
#(read about split() function of string).
# Function should accept argument and return the changed value

# def user_reverd(text):
#     text = text.split()
#     reversed_text = text[::-1]
#     return ' '.join(reversed_text)
# user_text = input('text: ')
# print(user_reverd(user_text))

#2Write a function that takes a tuple as an argument and returns reversed one.
# def revers_tup(tuple):
#     return tuple[::-1]
# t = (1,2,3,4,5,6)
# print(revers_tup(t))

#3 Write a function to sum the area of a triangle. It should take two parameters
# def tringle(height , base):
#     S = 1/2 * height * base
#     print(f'S = 1/2 * {height} * {base}')
#     return f'Area of a triangle is S >> {S}'
# h = int(input('our height: '))
# b = int(input('our base: '))
# print(tringle(h,b))

#4Write a Python function that accepts a string
#and calculate the number of upper case letters and
#lower case letters

# def upper_lower(text):
#     u = 0
#     l = 0
#     for char in text:
#         if char.isupper():
#             u += 1
#         elif char.islower():
#             l += 1
#     return (f"our text:>> '{text}'\n"
#             f"Uppercase latters:{u}\n"
#             f"Lowercase letter:{l}")
# x = input("text:")
# print(upper_lower(x))