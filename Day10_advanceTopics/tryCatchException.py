def abc(): 
    try:
        print(3+1)
        return 7
    finally:
        return 9
    return 3


print(abc())


def AssertCheck():
    try:
        assert (2+3) == 6
        print("statement is true")
    except AssertionError:
        print("False assertion")
    finally:
        print("this wil print anyhow")

AssertCheck()

