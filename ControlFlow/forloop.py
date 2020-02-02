"""
For Loop
and looping through strings,list,tuple,dictionary
"""
my_string="abcdefghijklmno"

for c in my_string:

    if(c=="g"):
        print('G')
    else:
        print(c, end=" ")  ## am not aksing to print in new line ..so using end am saying print with " "

cars=['bmw','honda','benz']
for car in cars:
    print(car)

nums=(1,2,3,4,5,6)
for num in nums:
    print(num*10, end=" ")

dict={'name':'Hari','age': 33,'complex':'fair'}
for k in dict:
    print(k) ## by default keye are printed
    print(dict[k])

for k,v in dict.items():
    print(k,v)

print("^^"*20)
## Zipping functoin

l1=[1,2,3,4]
l2=[22,33,44,55,66,77,88,99]

for a,b in zip(l1,l2): ## stops at the shorter list , here l1 has 4 itesm so they both will print for 4 times and stops
    print(a," ", b)



