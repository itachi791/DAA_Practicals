#Iterative
def fibo(n):
    if n <= 1:
        return n
    myFib = [0, 1]  # Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1
    for i in range(2, n + 1):  # Start at 2, go up to n (inclusive)
        num = myFib[i - 1] + myFib[i - 2]
        myFib.append(num)
    print(myFib)

    return myFib[n]

# Example Usage
n = 10
print(f"Fibonacci number at position {n}: {fibo(n)}")

#Recurisve
def rec_fibo(n):
    # Base case: Fibonacci of 0 or 1
    if n <= 1:
        return n
    else:
        return rec_fibo(n - 1) + rec_fibo(n - 2)

# Example Usage
n = 10
print(f"Fibonacci number at position {n}: {rec_fibo(n)}")
