memo = {}

def fib(n):

    # Base cases
    if n == 0 or n == 1:
        memo[n] = n

    # if value hasn't been calculated, calculate it
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]

for _ in range(int(input())):
    print(fib(int(input())) % (10**9 + 7))
