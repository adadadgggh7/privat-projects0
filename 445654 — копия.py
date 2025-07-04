#1Write a Python program to construct the following pattern, using for loops. (image_1)

# symbol = '*'
# for symbol_rng in range(1,5):
# 	construct = symbol * symbol_rng
	# print(construct)
# for symbol_rng in range(4,0,-1):
# 	construct = symbol * symbol_rng
# 	print(construct)

#2Write a python program to count number of even  digits in a  number (ex: 2135 >>> 1)
# numb_=int(input('our number\n'))
# cycle = 0
# for x in str(numb_):
# 	if int(x) % 2 == 0:
# 		cycle += 1
# print(cycle)

#3Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number(image_2)

# first = 0
# sum_ = 0
# for second in range(0,11):
# 	prev = first
# 	sum_ = first + second
# 	first = second
# 	print(f'{prev}+{second}={sum_}')

#4Given a string, display only those characters which are present under even index number.
text = input('text\n')
x = len(text)
for y in range(0,int(x),2):
	print(text[y])

