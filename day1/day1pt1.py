import numpy as np
filename = 'dataDay1.txt'
data = np.loadtxt(filename, delimiter='\n', dtype=int)
increase = 0

for idx, i in enumerate(data): 
    if data[idx-1] != None: 
        if data[idx -1] < i: 
            increase +=1

print(increase)