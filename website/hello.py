import random

r_num = random.randint(1,9)

while True:
    num = input('guess number between 1 to 9:')
    if num == 'exit':
        break
    num = int(num)
    if num == r_num:
        print('win')
        break
    elif num > r_num:
        print('its too big')
    elif num < r_num:
        print('its too small')