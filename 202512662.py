#Recursive Factorial Function
def factorial(n):
    if n == 0 or n ==1:
        return  1
    else:
        return n * factorial(n-1)
    
# Recursive Fibonnaci Function
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
#Main Program
n = int(input("Enter a number: "))

# Factorial Output
print("Factorial of", n, "=", factorial(n))

#Fibonnaci Output
print("Fibonnaci sequence: ")

for i in range(n):
    print(fibonnaci(i), end=" ")