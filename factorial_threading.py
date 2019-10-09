from threading import  Thread

threadId = 1


def factorial(n):
   global threadId
   if n < 1:   # base case
       print ("%s: %d" % ("Thread", threadId ))
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

s1=Thread(target = factorial,args=(5))
s2=Thread(target = factorial,args=(4))



s1.start()
s2.start()

s1.join()
s2.join()

#c = input("Waiting for threads to return...\n")
