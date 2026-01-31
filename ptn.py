def bargraph(n):
    r=max(n)
    c=len(n)
    for i in range(1,r+1):
        for j in range(1,c+1):
            if r-n[j-1]>=i:
                print('  ',end='')
            else:
                print('*  ',end='')    
        print() 

n=[2,6,4,0,5]
bargraph(n)