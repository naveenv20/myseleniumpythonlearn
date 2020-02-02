"""
loops
"""

#************* WHILE ******************
x=20
while(x>10):
    print("The value of : %i  " %(x))
    x=x-1

print("#"*20)
l=[]
num=0
while num<10:
    l.append(num)
    print("value of num is ",num)
    num+=1

print(l)
print("#"*20)
# Break and continue

#Break: To nreak out of the closest enclosing loop

# Continue: Go to the start of the closest enclsoing loop

"""
Break
"""
num=0
while num<10:

    print("value of num is ",num)
    num += 1

    if(num==5):
        print("We are at 5")
        break
    print("after if loop")
    print("$" * 20)
print("After while")

"""
Continue
"""
print("#@"*20)
num=0
while num<10:

    print("value of num is ",num)
    num += 1

    if(num==5):

        continue
        print("We are after continue 5")
    print("after if loop")
    print("$" * 20)
else:
    # else after the while ( Not like if case ) in if only if the condition on if is not satisified then else part will come hre after the while it will print
    # ****One check is if loop is existing because of break then ... else wont be executed
    print("After while is done then it will come to this else***************")
