
# def fibonacci(n):

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))  
# print(fibonacci(1))  
# print(fibonacci(6)) 
# print(fibonacci(9)) 
# print(fibonacci(35)) 

# Fibonacci using loop 

def fibonacci_loop(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    i = 2

    while i <= n:
        a, b = b, a + b
        i += 1

    return b

print(fibonacci_loop(0)) 
print(fibonacci_loop(1))  
print(fibonacci_loop(6)) 
print(fibonacci_loop(9))  
print(fibonacci_loop(35)) 