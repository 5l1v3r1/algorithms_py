# Algorithm that generates random positions for elements of an array from 0-10
# without the use of the random library
# does not work with arrays bigger than 11 (0-10) 
from datetime import datetime # datetime.now() is used to generate "random" numbers
from time import sleep

#generate an array with 11 elements, all of them being -1
arr = [-1 for i in range(0, 11)] 

j = 0
while j <= 10:
    t = int(str(datetime.now())[25])
    sleep(0.005)
    if t not in arr:
        arr[j] = t
        j+=1
    elif j == 10:
        if int(str(datetime.now())[25]) != 0:
            arr[j], arr[t] = arr[t], 10 
        else:
            arr[j] = 10 
        j+=1

print(arr)

# Example outputs:
# [10, 1, 0, 7, 5, 3, 9, 8, 4, 2, 6]
# [7, 6, 4, 1, 0, 5, 10, 9, 3, 8, 2]
# [3, 1, 8, 10, 5, 2, 6, 9, 4, 0, 7]