
def Distinct(lst):
    count_map = {}
    for num in lst:
        abs_num = abs(num)
        if abs_num in count_map and abs_num != 0:
            count_map[abs_num] += 1
        else:
            count_map[abs_num] = 1
    
    distinct_count = 0
    for value in count_map.values():
        distinct_count += min(value, 2)
    
    return distinct_count, count_map




x = input('').split(' ')
n = eval(x[0])
m = eval(x[1])
P = eval(x[2])
y = input('')
y = [int(num) for num in y.split()]
array = [int(num) for num in y]
distinct, count = Distinct(array)
Sum = 0
for i in range(n):
    Sum += array[i]
for _ in range(m):
    z = input('')
    z = [int(num) for num in z.split()]
    lis = [int(num) for num in z]
    if lis[0] == 1:
        k = lis[1]
        x = lis[2]
        y = lis[3]
        c = lis[4]
        old = array[k - 1]
        list1 = []
        list2 = []
        new = ((x ** 2 + k * y + 5 * x) % P) * c
        
                
            
        
        
        
        if abs(new) != abs(old):
            count_old = count[abs(old)]
            try:
                count_new = count[abs(new)]
            except:
                count_new = 0
        
            
            if (count_old == 2  and old != 0) or count_old == 1:
                distinct -= 1
            if count_new == 0 or (count_new == 1 and new != 0 ):
                distinct += 1
        array[k - 1] = new
        diff = new - old
        Sum += diff
        count[abs(old)] -= 1
        try:
            
            count[abs(new)] += 1
        except:
            count[abs(new)] = 1

    elif lis[0] == 2:
        print(Sum)
        
    elif lis[0] == 3:
        
        print(distinct)
