# from https://www.freecodecamp.org/news/if-name-main-python-example/

# python one module
# import only fn three from file_two
from file_two import function_three

print("File one __name__ is set to: %s" % (__name__))


def function_one():
    print("Function one is executed")


def function_two():
    print("Function two is executed")


if __name__ == "__main__":
    print("File one executed when ran directly")
    function_two()
    function_three()
else:
    print("File one executed when imported")
