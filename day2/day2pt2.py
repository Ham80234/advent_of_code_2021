#test = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
import numpy as np
filename = 'dataDay2.txt'
data = np.loadtxt(filename, delimiter='\n', dtype=str)


horizontal = 0 
verticle = 0 
aim = 0     
result = horizontal * verticle

for i in data: 
    item = i.split(' ')
    if item[0] == 'forward': 
        horizontal += int(item[1])
        verticle += aim * int(item[1])
    if item[0] == 'up': 
        aim -= int(item[1])
    if item[0] == 'down': 
        aim += int(item[1])

print(horizontal, verticle, horizontal*verticle)