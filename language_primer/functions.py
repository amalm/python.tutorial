def fib(n = 1000):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Now call the function we just defined:
print(fib(2000))
#or assign it to a var
f100 = fib(100)
print(f100)

#default argument
print(fib())

#if documented with docstrings, get help on the function
print(help(fib))
