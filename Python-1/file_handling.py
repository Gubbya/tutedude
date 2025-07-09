#f = open('data.txt', 'r')
f = open('data.txt', 'r+') 
g = open('data.txt', 'r')
h = open('data.txt', 'r')


#read the entire file
data = f.read()
print(data)

data1 = g.readlines()
print(data1) 
print(data1) 



data2 = h.readline()
print(data2)

#write to the file
f.write("\nThis is a new line added to the file.\n")

f.close()
g.close()
h.close()
# Close the file handles to free up resources
