a = 10
b = 2
c = a / b
print(c)
# This code takes an integer input from the user and prints it
# The input is expected to be an integer, and it will raise an error if the input is not an integer
# If you want to handle the error, you can use a try-except block
d = int(input("Enter a number: "))
try:
    # This code attempts to divide a by d
    # If d is zero, it will raise a ZeroDivisionError
    # To handle this error, you can use a try-except block
    e = a/d  ## This line will raise an error if d is zero
## To avoid division by zero, you can check if d is zero before performing the division 
    print("Result of division:", e)
   # print(e)
    
except:
    print("Error: Division by zero is not allowed.")
    
