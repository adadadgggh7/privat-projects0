#chinga chung 
import random 
first_start = input('hello wanna ply game with me press 1 \n')
pc_win = 0
you_win = 0
drow = 0
print('press 1 for Rock 2 for paper and 3 for scizer')
if first_start == '1':
  Game_end = True 
  while Game_end:
    user_coisce=input('input you number \n')
    if user_coisce.isdigit():
      user_coisce=int(user_coisce)
      if user_coisce not in range(1, 4):
        print('your number need to be in range 1-3 \n')
        continue
  
      pc_rane=random.randint(1,3)
      if pc_rane == user_coisce:
          print('draw')
          drow += 1
      elif (user_coisce == 1 and pc_rane == 3) or \
      (user_coisce == 2 and pc_rane == 1) or \
      (user_coisce == 3 and pc_rane == 2 ):
        print('user win')
        you_win +=1
      else:
        print('i win')
        pc_win += 1

      continu_e = input('wanna continue press 1 \n')
      if continu_e != '1':
        print('all right')
        Game_end = False
        print(f'plaid game {you_win+pc_win+drow}')
        print(f'your win {you_win}\n'\
          f'times i win {pc_win}\n'\
          f'drow {drow}')
      else:
        ('you number needs to be digit')
        continue
else:
  print('good bay')