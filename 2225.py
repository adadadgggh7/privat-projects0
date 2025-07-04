import os
#make new file if you didnt have
file = open('data.txt', 'w')

print('hello tell us about you if you end it just input x for end')

def namesinput():
    while True:
        info = input('names/surname: ')
        if info == 'x':
            break
        hobby = input('your hobby: ')
        if hobby == 'x':
            break
        file.write(f'{info} \n{hobby} \n')

#append new text
def append():
    while True:
        question = input('are you miss something wanna add  yes/no ? \n')
        if question == 'no':
            print('ok')
            break
        else:
            newappend = input('append what you miss: ')
            file = open('data.txt','a')
            file.write(newappend)
#check all lines
def check():
    file = open('data.txt', 'r')
    l = 0
    for x in file:
        l += 1
def checkwrdacha():
    file = open('data.txt')
    text = file.read()
    words = len(text.split())
    chars = len(text)
    return words,chars


namesinput()
append()
l = check()
words,chars = checkwrdacha()
file = open('data.txt', 'r')
print(f'\n{file.read()} \nrow numbers {l}'
      f'\nwords count {words} \t char {chars} count')

file.close()

