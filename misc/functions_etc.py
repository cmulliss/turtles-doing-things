# Trying things out
# global and local variables

message1 = 'Global Variable'

def myFunction():
    print('\nINSIDE THE FUNCTION')
    #global variables are accessible within a function
    print(message1)
    #declaring a local variable
    message2 = 'Local Variable'
    print(message2)

#calling the function
myFunction()

print('\nOUTSIDE THE FUNCTION')
#Global variables are accessible outside the function
print(message1)

#Local variables are NOT accessible outside the function
print(message2)
    
