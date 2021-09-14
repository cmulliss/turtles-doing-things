# python module to import
# if file two has 2 fns, but we only want to import one of them

print("File two __name__ is set to: %s" % (__name__))


def function_three():
    print("Function three is executed")


def function_four():
    print("Function four is executed")


if __name__ == "__main__":
    print("File two executed when ran directly")
else:
    print("File two executed when imported")
