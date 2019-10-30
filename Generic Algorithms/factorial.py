
def factorial(n):
    """Algorithm for factorial."""
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factorial_r(n):
    """Recursive factorial algorithm."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#%%
factorial_r(4)













