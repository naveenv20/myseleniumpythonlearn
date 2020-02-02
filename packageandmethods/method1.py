"""
methods demo
"""


def sum_nums():
    print(2 + 3)


sum_nums()


def sum_variables(n1, n2):
    """
    Documentation-- this method is used to add two variables
    :param n1:
    :param n2:
    :return: the added value
    """

    # print(n1+n2)
    return (n1 + n2)


sum1 = sum_variables(2, 3.5)
sum2 = sum_variables("sai", "ram")
print(sum1)
print(sum2)

print("*" * 20)


def is_metro(city='nyc'):
    """

    :param city: given a default vaiue to nyc
    :return:
    """
    l = ["sfc", "la", "nyc"]

    if city in l:
        return True
    else:
        return False


x = is_metro("Guntur")
print(x)


print(is_metro()) # coming because default city is nyc and its metro ..so true


print(is_metro(city='BZA')) # other way of calling ... and position of parametr doesnt matter .. u can call by specifically assigning these

