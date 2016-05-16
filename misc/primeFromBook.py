# Trying things out
# Functions, def and return

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
        return True
    
answer = checkIfPrime(77)
print(answer)
