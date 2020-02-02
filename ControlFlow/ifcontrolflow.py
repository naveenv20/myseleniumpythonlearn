"""
condition logic
"""

a=100
b=10
if(b<a):
    print("%s less than %s"%(a,b))

print("This iwll always print")

val='Green'
value=val

if(value=='Red'):
    print("Stop")
elif(value=='Green'):
    print("Not in if so elif")

else:
    print("Not in if or elif so inside else")