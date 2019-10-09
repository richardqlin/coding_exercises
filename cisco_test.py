a = 'aab2(c)e3(df)'

out = 'aabccedfdfdf'

o = []
c = []

d = 0

f = 0

for i in a:
    print(c)
    if i.isdigit():
        s=int(i)
    elif i =='(' and f ==0:
        f =1
        #o.append(i)
    elif i.isalpha() and f ==1:       
        c.append(i)
    elif i == ')':
        f =0
        d = 1
    elif d == 1:
        s-= 1
        for i in c:
           
            o.append(i)
        if  s <=0:
            d=0
            c=[]
        
    elif i.isalpha():
        o.append(i)

print (o)

b = []


