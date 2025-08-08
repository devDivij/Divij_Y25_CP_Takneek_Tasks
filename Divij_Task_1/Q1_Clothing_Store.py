# cook your dish here
n= int(input())

for i in range(0,n):
    count = 0
    x,y,z,a,b,c=[int(s) for s in input().split()]
    
    for l in range(0,a):
        if x>0:
            x-=1
            count+=1
        elif y>0:
            y-=1
            count+=1
        elif z>0:
            z-=1
            count+=1
    for m in range(0,b):
        if y>0:
            y-=1
            count+=1
        elif z>0:
            z-=1
            count+=1

    for n in range(0,c):
        if z>0:
            z-=1
            count+=1
    print(count)
    