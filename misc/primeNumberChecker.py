# Trying things out
# Functions, def and return

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
        return True
    
userInput = int(input('Enter a number: '))
answer = checkIfPrime(userInput)
print(answer)
