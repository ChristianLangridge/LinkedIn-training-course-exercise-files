def factorial(num):
    if type(num)!= int or num < 0:
        return None
    if num == 0:
        return 1
    return num * factorial(num - 1) 
    

print(factorial(5))
print(factorial(6))
print(factorial(-3))
print(factorial(1.3))
print(factorial("10"))