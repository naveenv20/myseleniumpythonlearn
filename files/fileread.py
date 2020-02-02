"""
read files
.read()
.readline()
"""

my_file=open("first_file.txt","r")

# .read(0 function reads the full file
print(str(my_file.read()))

my_file.close()

print("line by line==============>")

my_file_line=open("first_file.txt","r")
# read one line of the file
print(str(my_file_line.readline()))
# reads the second line
print(str(my_file_line.readline()))

my_file_line.close()