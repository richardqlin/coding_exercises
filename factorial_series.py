def fact(n):
    if n<=1: return 1;
    else: return n*fact(n-1)

print(fact(10))

def fib(n):
    if n<2: return n;
    else: return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])
