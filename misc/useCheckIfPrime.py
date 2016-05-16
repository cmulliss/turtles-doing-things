#This doesn't work properly, needs some revision later

import sys
if '/Users/cherry/Desktop/repos/turtles-doing-things/misc/modules' not in sys.path:
    sys.path.append('/Users/cherry/Desktop/repos/turtles-doing-things/misc/modules')
    
import prime

numberToCheck = int(input('Please enter a number: '))
answer = prime.checkIfPrime(numberToCheck)
print(answer)

answer = prime.checkIfPrime(numberToCheck)
print(answer)


