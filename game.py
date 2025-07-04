import os
import time
import keyboard

# Initial position of the car
position = 10
width = 30  # Width of the road
print('\t\t\t( ( )')
def draw_road(position):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    road = [' '] * width
    road[position] = '8==D'
    print(''.join(road))

print("Use ← and → arrows to move the car. Press 'q' to quit.")

while True:
    draw_road(position)
    time.sleep(0.1)

    if keyboard.is_pressed('right') and position < width - 1:
        position += 1
    elif keyboard.is_pressed('left') and position > 0:
        position -= 1
    elif keyboard.is_pressed('q'):
        break
