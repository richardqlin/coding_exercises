l=[2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]

l1=[4, 4, 2, 2, 2, 2, 3, 3, 1, 1, 6, 7, 5]

def sorted_list(l):
    d={}

    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    print(d)

    sorted_d= sorted((value, key) for (key,value) in d.items())
    
    sorted_d.reverse()
    for i in sorted_d:
        for j in range(i[0]):
            print(i[1],end= ' ')
    print()

sorted_list(l)


sorted_list(l1)
