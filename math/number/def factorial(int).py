def factorial(number):
    factorial = 1
    for num in range(number,1,-1):
        factorial = factorial * num
    return factorial

print(factorial(100))
