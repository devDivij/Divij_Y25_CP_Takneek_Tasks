# cook your dish here
t=int(input())
for i in range(0,t):
    n,c = input().split(' ')
    c = int(c)
    s= input()
    temp= list(s)
    E = ['A','B','C','D',"E"]
    e = []
    cost = 0
    for i in range(0,5):
        q=temp.count(E[i])
        e.append(q)
    e.sort(reverse=True)
  
    def series_sum(p):
        return p*(p+1)/2
    
    for i in range(0,5):
        if c+series_sum(sum(e[i+1:]))>series_sum(sum(e[i:])):
            cost+=series_sum(sum(e[i:]))
            break
        else:
            cost+=c
    print(int(cost))