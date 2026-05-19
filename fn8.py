
def double(x):
    return x * 2

def apply_twice(func, value):
    return func(func(value))

print(double(3))               
print(apply_twice(double, 3))   
print(apply_twice(double, 5))   