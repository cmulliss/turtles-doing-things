inputFile = open ('myFile.txt', 'r')
outputFile = open ('myOutputfile2.txt', 'w')

msg = inputFile.read(10)

# to prove only reads 10 bytes at a time add newline
while len(msg):
  outputFile.write(msg + '\n')
  msg = inputFile.read(10)
inputFile.close()
outputFile.close()
    
