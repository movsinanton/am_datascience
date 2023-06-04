"""The game"""
import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input("type your number"))
    if predict_number > number:
        print('need less')
    elif predict_number < number:
        print('need more')
    else:
        print(f'Yes, this is {number}, {count} takes')
        break