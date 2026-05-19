
def total(*args, multiplier=1):

    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum * multiplier

print(total(1, 2, 3))                     
print(total(1, 2, 3, multiplier=2))       
print(total(10, 20, multiplier=3))         