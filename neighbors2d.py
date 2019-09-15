from random import choice
n=200
count=0 #counts total number neighbors that a particular cell has
nocc=0
list2d=[[choice((0,1)) for x in range(n)] for y in range(n)]
for x in range(1,n-1):
    for y in range(1,n-1):
        if list2d[x][y]==1:
            nocc+=1
            neigh=list2d[x-1][y]+list2d[x+1][y]+list2d[x][y-1]+list2d[x][y+1]#sum of the four neighboring cells
            if neigh > 2:
                count+=1
print("Fraction with more than 2 neighbors:",count/nocc)