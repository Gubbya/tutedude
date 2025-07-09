#file= open("onlyRead.txt", "r")  # Open the file for reading only
#data = file.read()  # Read the content of the file
#print(data)  # Print the content of the file
#file.close()  # Close the file after reading    
                # Note: This code assumes that "onlyRead.txt" already exists and contains some text.
                # If the file does not exist, it will raise a FileNotFoundError.    

try:
    file = open("onlyRead.txt", "r")  
    print("\n The file 'onlyRead.txt' does exist.\n")
    data = file.read()
    print(data)       
except FileNotFoundError:
     print("The file 'onlyRead.txt' does not exist.")
except Exception as e:
     print(f"An error occurred: {e}")
# This code opens a file named "OnlyRead.txt" in read mode, reads its content, and prints it to the console.
# If the file does not exist, it catches the FileNotFoundError and prints an error message.
# It also includes a general exception handler to catch any other errors that may occur.            