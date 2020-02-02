"""
Strings--seq of charc

"""

a="Sai ram"
b='sai Krishna'

print(a)
print(b)

c="Sai ram 'quotes' is devotional" # quotes inside qyotes first given " then used '
print(c)

d="Sai ram \"quotes\" is devotional" # using escapre character here \ before "
print(d)


print(a[0]) # 0th index is S

"""
len()
lower()
upper()
str()
"""
print(a.lower())
print(a.upper())
print(len(a))

#print(a+2)  Cant add number and string

print(a+str(2)) # type casting the number 2 to string


"""
concat
"""
print(a+"  "+b)

"""
replace
"""
a1="1abc2abc3abc"
print(a1.replace('abc','ABC'))

"""
replace with count
"""
print(a1.replace('abc','ABC',2)) #only the first 2 instances are changed

"""
Sub strings

"""
sub=a1[1:5]
print(sub) # starting index is inclusive and ending index is exclusive ===> abc2

#sub string iwth steps
sub2=a1[1:7:2]
print(sub2)# abc2ab with step 1 , and as this is with step 2, so the value is aca


sub3=a1[1:] # from 1 to end of the string
print(sub3)

sub4=a1[:8] # from starting to 7th character
print(sub4)

# other way
sub5=a1[-1]
print(sub5) # last character

sub6=a1[:-1]
print(sub6) # leaving the last character --total string  upper bound is exclusive so no last character above

sub7=a1[:len(a1)-1]
print(sub7)

sub8=a1[::] #total
sub9=a1[::2] # insteps of 2
print(sub9)

sub10=a1[::-1] # this is like reversing steps
print(sub10)


"""
String doesnt support item assignment
"""

a1[2]="t" # will give u error
print(a1)

