def factorial(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return (factorial(n-1)+(factorial(n-2)))
  
    

print(factorial(7))
