def fibonacci_until(end):
    fib = [0, 1]
    i = 2
    while fib[i-1] < end:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    return fib
end = int(input("Enter end of sequence: "))
fib_until = fibonacci_until(end)
print(fib_until)
