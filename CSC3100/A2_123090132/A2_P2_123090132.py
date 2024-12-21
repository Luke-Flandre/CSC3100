t = eval(input(''))
fcount = 0
ecount = 0
tc = 0
tclist, tcliz = [], []
zlist = []
x0 = 1
for _ in range(t):
    L = eval(input(''))
    for _ in range(L):
        
        a = list((input('').split()))
        

        
        if a[0] == 'F':
            fcount += 1
            
            x = a[2]
            y = a[3]
            if (x.isdigit() is False) and y.isdigit():
                    x0 = 0
            if x0 == 0:
                    zlist.append(0) 
            elif x == y or y.isdigit() or x == 'n':
                    zlist.append(0) 
                    
            elif x.isdigit and y == 'n':
                    zlist.append(1) 
                    tc += zlist[-1]
            
            
            
            

        elif a[0] == 'E':
            ecount += 1
            
            tcliz.append(tc)
            tc -= zlist[-1]
            zlist.pop(-1)
            
            
            if ecount == fcount:
                tca = max(tcliz)
                tclist.append(tca)
                tcliz = []
                tc, tca = 0, 0
                x0 = 1
                if fcount + ecount == L:
                    tcb = max(tclist)
                    if tcb == 0:
                        print('O(1)')
                    else:
                        print(f'O(n^{tcb})')
                    tcb = 0
                    ecount, fcount = 0, 0
                    tclist = []
