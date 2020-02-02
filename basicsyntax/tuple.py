"""
like  list but immutable
define using ()
"""
mylist=[1,2,3]
mytup=(1,2,3,4,5,6,7,8,4,0)
print(mylist)
print(mytup)

mylist[1]=4 # item assignment good
#mytup[1]=6 # Not ok immutsble

print(mytup[:-1])
print(mytup[2:8]) # lower bond inclusive ...upper bound exclusive

print(mytup.index(7))# gets u tthe index of 7


print(mytup.count(4)) # give u count of 4 in the tuple