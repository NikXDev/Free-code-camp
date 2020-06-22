# READING FILE
# file = open("employee.txt", "r")
# this statement tells whether file is readable or not
# print(file.readable())

print("..............")
# this reads the file
# print(file.read())

print("..............")
# this reads a single line
# print(file.readline())

print("..............")
# this takes entire data and puts it in a list
# print(file.readlines())

print("..............")
# this takes index of line to be displayed
# print(file.readlines()[3])


# WRITE FILE
# file1 = open("employee.txt", "a")
# file1.write("\nKelly - Customer Service")
# file1.close()

# to overwrite a file, replaces everything with current one
file1 = open("employee.txt", "w")
file1.write("\nKelly - Customer Service")
file1.close()
