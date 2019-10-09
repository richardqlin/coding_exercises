n = int(input("N? "))
primes = list(range(2, n + 1))
marked = [False] * len(primes)
p = primes[0]
while True:
    if 2 * p not in primes:
        break
    for i in range(primes.index(2 * p), primes.index(n) + 1, p):
        marked[i] = True
