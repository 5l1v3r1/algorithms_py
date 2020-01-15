# selection sort algorithm

def sort(l):
    for i in range(len(l)):
        min_num = l[i]
        for j in range(i+1, len(l)):
            if l[j] < min_num:
                min_num, l[j] = l[j], min_num
        l[i] = min_num

    return l

print(sort([3,2,4,1]))