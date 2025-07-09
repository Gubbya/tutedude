def hello_world():
    print("Hello, World!")
    return "hey Buddy"
a = hello_world()
print(a)


#functions are first class objects in Python, meaning they can be assigned to variables, passed as arguments, and returned from other functions.

new = hello_world
#print(new) #will get error because new is a function, not a string
# To call the function new, you need to use parentheses
#print(new())
b = new ()
print(b)

#single arument function
def add_two_numbers(x):
    return x + 2
b = add_two_numbers(5) # here 5 is the argument passed to the function add_two_numbers x value is 5
print(b)

# function with two arguments
def add_numbers(g, f):
    c = g + f
    return c
f = add_numbers(10,15) # this f and different from the f in the previous function add_numbers(g, f)
print(f)
 
 # function inside a function
def outer_function():
     def inner_function():
         return "Hello from the inner function!"
     return inner_function()
a = outer_function()
print(a)
#print inner_function()  # This will raise an error because inner_function is not defined in the global scope
  