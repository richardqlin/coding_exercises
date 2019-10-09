import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s_x = sorted(x.items(), key=operator.itemgetter(1))

print (s_x)

print(zip(s_x))

y=zip(s_x)

for i in y:
    print (i)


key_value ={}     

# Initialize value  
key_value[2] = 56       
key_value[1] = 2 
key_value[5] = 12 
key_value[4] = 24
key_value[6] = 18      
key_value[3] = 323 
print(key_value)

a=list(key_value.values())
a.sort()
a.reverse()
print(a)
for i in a : 
    print (i, end =" ") 
