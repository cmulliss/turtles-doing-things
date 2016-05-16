f = open('myFile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline, end = '')
print(secondline)

f.close()

# appending to file

f = open('myFile.txt', 'a')
f.write('This sentence will be appended')
f.write('\nPython is fun!')
f.close()

# or using a for loop

f = open('myFile.txt', 'r')
for line in f:
    print(line, end = '')
f.close




