def mergeSort(arr):
    if len(arr) > 1:
        mid =len(arr)//2
        l=arr[:mid]
        r= arr[mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0
        #copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        # checking if any element was left

        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1

        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1



# code to print the list

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()

arr = [12,11,13,7,6,5]

printlist(arr)

mergeSort(arr)

printlist(arr)
        

            
