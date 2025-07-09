#file = open("read_write.txt", "w") # this will create a new file or overwrite an existing one
#file = open("read_write.txt", "w+") # Open the file for reading and writing, creating exist but still overwriting if it does.
#file = open("read_write.txt", "r+") # Open the file for reading and writing, creating it if it doesn't exist but still overwriting if it does.
#file = open("read_write.txt", "x+")  # Create for reading and writing, fail if file exists
try:
    file = open("read_write.txt", "x+")  # Try to create a new file for reading and writing
    print("File 'read_write.txt' created successfully.")
except FileExistsError:
    print("\n File already exists. Not overwriting.")
    file = open("read_write.txt", "r+")  # Open for reading and writing if it exists
# Check if the file was created successfully

data = file.read()  # Read the content of the file
#file.seek(0)        # Move the cursor to the beginning of the file before reading

if file.tell() == 0:  # If the file is empty, we can write to it
    print("File is empty, writing sample content. \n")
    file.write("Hello, this is a sample file.\n")
    file.write("This file was created using Python!\n")
    file.write("You can add more lines as needed.\n")
else:  # If the file is not empty, we can read its content
    print("File already has content. Reading existing content.")

file.seek(0)        # Move the cursor to the beginning of the file to read again
data = file.read()  # Read the content of the file
print(data)

 
new_Line = input("Enter whatever you want: ") # Prompt the user to enter a new line to add to the file

file.seek(0, 2)  ## move the cursor to the end of the file before writing
file.write(new_Line + "\n")
file.seek(0)    # Move the cursor to the beginning of the file to read again
data = file.read()  # Read the content again after seeking
print("\n *******************Newly edited file***********************\n")   
print(data)
file.close()    # Close the file to save changes
#print("File 'sample_file.txt' has been created and content written successfully.")