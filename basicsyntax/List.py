"""
List are defined in brackets and separated by , [1,2,3,4]
# Mutable
"""
cars=['honda','mazda','audi','toyota','bmw']
empty_list=[]
print(cars)
print(empty_list)
print(type(cars))

print(cars[0])
print(cars[1:3])
print(cars[:-2])
print(cars[::2])
print(cars[::-1])

# assignement can be done
cars[2]="Ford"
print(cars)

# adding an extra value at the end
cars.append('Nano')
print(cars)

# adding a value at the required position
cars.insert(1,"Jeep")
print(cars)

# length of the list
print(len(cars))

# findig index of a value
print(cars.index('Nano'))

# Pop -rmeoves the item from list  at the end
print(cars.pop())
print(cars)

# remove the required item
cars.remove('Jeep')# this doent return any thing but removes the ite,m
print(cars)

# sorting
print("*#"*20)
cars.sort()
print(cars)