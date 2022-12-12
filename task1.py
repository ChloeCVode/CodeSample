#   Create a function that checks if a number n
#   is divisible by two numbers x AND y
#   All inputs are positive, non-zero numbers.

def is_divisible(n,x,y):
    a = n % x
    b = n % y
    if a == 0 and b == 0:
        return True
    else:
        return False
    
    
    
