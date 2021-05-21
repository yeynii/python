from functools import cmp_to_key

def my_compare(x,y):
    if int(x + y) > int(y + x):
        return -1
    else:
        return 1
    
def solution(numbers):
    str_numbers = list(map(str, numbers))
    if all(s == '0' for s in str_numbers):
        return '0'
    str_numbers = sorted(str_numbers, key= cmp_to_key(my_compare))
    return "".join(str_numbers)
