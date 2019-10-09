def count(S,m,n):
    table = [[0 for x in range(n+1)] for y in range(n+1)]

    for i in range(m):
        table [0][i] = 1

    for i in range(1,n+1):
        for j in range(m):
            x = table[i - S[j]][i] if i - S[j] >= 0 else 0
                      
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x+ y
        
    return table

arr= [1,2,3]

m = len(arr)

n = 4
x = count(arr,m,n)
print(x)
