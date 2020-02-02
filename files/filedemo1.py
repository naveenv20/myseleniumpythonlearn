"""
File I/O

w-> write only mode
r-> read only mode
r+-> read and write mode
a-> append mode

"""

my_list=[1,2,3,4,5]


# opening the file in the write mode
my_file=open("first_file.txt","w")

#for each item in my_list
for i in my_list:
    # uisng the commnad write(), we are writing into th efile
    # write takes a string argument
    my_file.write(str(i)+ "\n")

#python writes in buffer and then later writes to file 
my_file.close()