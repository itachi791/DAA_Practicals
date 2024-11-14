# Iterative Fibonacci function with step count
def fibo(n):
    steps = 0  # Initialize step counter
    myFib = [0, 1]
    for i in range(2, n):  # Start from the third Fibonacci number
        steps += 1  # Count each iteration
        num = myFib[i - 1] + myFib[i - 2]
        myFib.append(num)
    return myFib[:n], steps  # Return Fibonacci sequence and step count

# Recursive Fibonacci function with step count
def rec_fibo(n, steps=0):
    steps += 1  # Count each recursive call
    if n <= 1:
        return n, steps  # Return the result and steps taken so far
    else:
        fib1, steps1 = rec_fibo(n - 1, steps)
        fib2, steps2 = rec_fibo(n - 2, steps1)
        return fib1 + fib2, steps2  # Return sum and total steps

# Ask the user for input
n = int(input('Enter a number to generate Fibonacci sequence up to: '))

# Call the iterative Fibonacci function
iterative_result, iterative_steps = fibo(n)
print(f"Iterative Fibonacci sequence up to {n} terms: {iterative_result}")
print(f"Steps taken (iterative): {iterative_steps}")

# Call the recursive Fibonacci function for the nth Fibonacci number
recursive_result, recursive_steps = rec_fibo(n - 1)  # nth Fibonacci number (0-indexed)
print(f"Recursive Fibonacci for the {n-1}th number: {recursive_result}")
print(f"Steps taken (recursive): {recursive_steps}")
