"""
Modules example
"""

# Import the module


import math as m

# other way for only sepcifc function
from math import  sqrt



class ModuleDemo():

    def builtin_modules(self):
        # using the math module sqrt function

        print(m.sqrt(144))
        print(sqrt(100))

e=ModuleDemo()
e.builtin_modules()