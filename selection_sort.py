import sys

a= [ 64, 25, 12, 22, 11]

for i in range(len(a)):
    mid_idx = i
    for j in range(i+1, len(a)):
        if a[mid_idx] > a[j]:
            mid_idx = j

    a[i], a[mid_idx] = a[mid_idx],a[i]


print(a)
print('Sorry array')

for i in range(len(a)):
    print('%d' %a[i])

