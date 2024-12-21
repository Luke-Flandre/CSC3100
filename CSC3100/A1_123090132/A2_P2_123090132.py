a= input('').split(' ')
b= input('').split(' ')
c= input('').split(' ')
d= input('').split(' ')



n = eval(a[0])
q = eval(a[1])
permutation = []
left = []
right = []
for _ in range(0, n):
    permutation.append(eval(b[ _]))
for _ in range(0,q):
    left.append(eval(c[_]))
    right.append(eval(d[_]))

def isValid(n, q, permutation, left, right):
    if permutation[0] != left[0] or permutation[n - 1] != right[0]:
        return False
    
    for i in range(q - 1, 0, -1):
        if permutation.index(left[i]) >= permutation.index(right[i]):
            return False
        if left[i] == left[i - 1]:
            x = permutation.index(left[i])
            y = permutation.index(right[i])
            z = permutation.index(right[i - 1])
            if (x < y and y < z) is False:
                return False
        if right[i] == right[i - 1]:
            x = permutation.index(right[i])
            y = permutation.index(left[i])
            z = permutation.index(left[i - 1])
            if (z < y and y < x) is False:
                return False
        if right[i] != right[i - 1] and left[i] != left[i - 1]:
            try:
                x = right.index(right[i])
                if x > i:
                    return False
            except ValueError:
                try:
                    y = left.index(left(i))
                    if y > i:
                        return False
                except ValueError:
                    return False
    
    return True

status = isValid(n, q, permutation, left, right)
if status == True:
    print(1)
else:
    print(0)
    
    
