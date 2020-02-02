"""
should ne in key value pairs
just like hashmap
{K1:V1, K2:V2 ,K3:V3}
values can be of any data type
not sequenced no idexing
mutable
"""
car={'make':'Mazda','year':2019,'model':'i touring'}
print(car)

emptydist={}
# pritning value
print(car['year'])
##--not possible print(car[0])


#pringting keys
print(car.keys())

#printing vaues
print(car.values())

print("*#"*20)
#printing items
print(car.items())

print(emptydist)

#add item
emptydist['car']='Audi'
emptydist['year']=2020
print(emptydist)

# assignment
emptydist['year']=2019
print(emptydist)

#nested dict
multicars={'bmw':{'make':'550i', 'year':'2019'},'mazda':{'make':'i touring', 'year':'2012'}}
print(multicars)

print(multicars['bmw'])

print(multicars['bmw']['year'])

# clearing the dict
#car.clear()--clears everything

# pop
print("*$"*20)
print(car)
print(car.pop('model'))
print(car)
