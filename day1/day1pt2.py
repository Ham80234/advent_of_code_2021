import numpy as np
filename = 'dataDay1.txt'
data = np.loadtxt(filename, delimiter='\n', dtype=int)
increase = 0


for i in range(4, len(data)+1): 
    first = data[i-4:i-1]
    second = data[i-3:i]
    if sum(first) < sum(second):
        increase += 1

print(increase)

