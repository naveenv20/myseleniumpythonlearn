"""
variable scope
"""

a=10
ab=15
def test_method(a):
    print("inside method local value is old ",a)
    a=a+2
    print("inside method local value is new", a)


print("before calling method",a)
test_method(a)
print("after calling method ", a)

print("&"*20)

def test_method2():
    global ab

    print("inside method2 local value is old ",ab)
    ab=ab+2
    print("inside method 2local value is new", ab)


print("before calling2 method",ab)
test_method2()
print("after calling2 method ", ab)


def test_method3(*args):
    """

    :param args: variable paramters
    :return:
    """

    return max(args)

print(test_method3(1,5,8,0,11,123))