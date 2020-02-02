"""
Different prints
"""
city='banglore'
event='cricket'
print("Welcome to the City :",city," for the event ",event) # one way
print("Welcome to the City :"+ city +" for the event "+ event) # another

# other way is
print("Welcome to the City : %s for the event %s "  %(city,event)) # good way

print("Welcome to the City : %s "  %(city))