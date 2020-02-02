"""
sample exceptions
https://docs.python.org/3/library/exceptions.html
"""
from csv import excel


def exception_hand():
    try:

        a = 10
        b = 20
        c = 10
        e = 0
        d = (a + b) / c
        print(d)
        # f=a/e # deliberately happeing an exception division by zero
        # print(f)
        print("@" * 20)
        g = a / "String"
        print(g)
    # except ZeroDivisionError:
    #     print("In the excep block --not possible--zero divisoin")
    # except TypeError:
    #     print("In the excep block --not possible--type error")
    except:
        print("in exceptoin block")
        ### RAISING the EXCEPTION
        raise Exception(" ***this is we raised the exception***")

    else:
        """
        This will be executed only when there is no exception
        """
        print("will be executed when there was no exception")
    finally:
        """
        Always executed
        """
        print("Always executed even when u execeptions")


exception_hand()
