count = [0]*10

flag =0
l=[]
while 1:
    a = input('entry')
    if a=='0':
        count[0] +=1
        
         
    elif a == '1' and count[0] >0:
        count[0] -=1
        
    print(count[0])
