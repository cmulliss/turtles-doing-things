# beware infinite loops with while loops, need to count down to false
#    counter = counter - 1

counter = 5

while counter > 0:
    print('Counter = ', counter)
    counter = counter - 1


# Using break, to exit entire loop when a condition is met

j = 0
for i in range(10):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j == 10:
        break

# continue used AFTER the keyword is skipped for that iteration

j = 0
for i in range(5):
    j = j + 2
    print('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print('I will be skipped over if j=6')

    
    

    
