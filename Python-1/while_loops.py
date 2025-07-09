for i in range(10):
    print(i)
    
# same thing with while loop
print("same thing with while loop")
i = 4 
while i < 10:
    
    print(i)
    i = i+ 1  # Increment i to avoid an infinite loop
    #i += 1  # Increment i to avoid an infinite loop
    #note: the while loop will run until the condition is false, so you need to make sure that the condition will eventually become false
# If you don't increment i, the loop will run forever, causing an infinite loop 
# Example of a while loop with a condition

print(" Example of a while loop with a break statement")
k = 0
while k < 10:
   if k == 5:
      break  # Exit the loop when k is equal to 5
print(k)
k += 1  # Increment k to avoid an infinite loop  