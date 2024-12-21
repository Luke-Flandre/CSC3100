from collections import deque

def min_deletion(A, n):
    N = (range(1, n + 1))    
    Ac = list(A)
    q = deque()
    Nc = list(N)
    
    a = 0
    for i in range(n):        
        if dic[i + 1] == 0:
            q.append(i)
            Nc[i] = 0
          
            dic[A[i]] -= 1
            
            a += 1
    while q:
        cur = Ac[q.popleft()]
        if Nc[cur - 1] == cur and dic[cur] == 0:
            q.append(cur - 1)
            Nc[cur - 1] = 0
            dic[A[cur - 1]] -= 1
            a += 1
   
    return a
               
n = eval(input(''))
A = input('')
A = [int(num) for num in A.split()]
dic = {}
for i in range(n):
    dic[i + 1] = 0
for num in A:
    
        dic[num] += 1
    
print(min_deletion(A, n))

