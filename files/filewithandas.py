"""
with and as

"""
#
# print("normal start")
# my_write=open("textfile","w")
# my_write.write("wrote first line")
# my_write.close()
#
# print("normal read")
# my_read=open("textfile","r")
# print(str(my_read.read()))

print("write as write start")

with open("withas.txt","w") as with_as_write:
    with_as_write.write("first line-sairam \n")
    with_as_write.write("second line-sairam\n")

print("#"*20)
print("With Read As Start")
with open("withas.txt","r") as with_as_read:
    print(str(with_as_read.read()))
