# Try, Except
#Usefull for error messages, need to come back to this

'''try:
    answer = 12/0
    print(answer)
except:
    print('An error occurred')
    '''

try:
    userInput1 = int(input('Please enter a number: '))
    userInput2 = int(input('Please enter another number: '))
    answer = userInput1/userInput2
    print('The answer is ', answer)
    myFile = open('missing.txt', 'r')
except ValueError:
    print('Error: you did not enter a number')
except ZeroDivisionError:
    print('Error: cannot divide by zero')
except Exception as e:
    print('Unkown error: ', e)
          

    


    
    

    
