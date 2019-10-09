words='Lists are one of the great datastructures in Python. We are going to learn a little bit about lists now. Basic knowledge of lists is requrired to be able to solve some problems that we want to solve in this chapter'

d={}

for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)



d={}

for i in range(5):
    d[i]=i*i

print(d)
