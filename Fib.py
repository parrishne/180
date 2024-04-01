# This is a python program to calculate the Fibonacci sequence. Create the code to do so below.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq

n = int(input("Enter the number of terms: "))
fibonacci_seq = fibonacci(n)
print(fibonacci_seq)


