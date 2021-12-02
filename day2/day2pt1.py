test = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
#import numpy as np
#filename = 'dataDay2.txt'
#data = np.loadtxt(filename, delimiter='\n', dtype=str)


horizontal = 0 
verticle = 0 
aim = 0     
result = horizontal * verticle

for i in test: 
    item = i.split(' ')
    if item[0] == 'forward': 
        horizontal += int(item[1])
    if item[0] == 'up': 
        verticle -= int(item[1])
    if item[0] == 'down': 
        verticle += int(item[1])

print(horizontal, verticle, horizontal*verticle)