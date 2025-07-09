a = open('student_grade.txt', 'r+') 

data = a.read()
print(data)

#a.write(input("Enter Student Name: ").)
#a.write.int(input("Enter Student Name: "))
new_Student = input("Enter Student Name: ")
a.write(new_Student + "\n")
a.close() 

