#!/usr/bin/python
# declare penguins and give it members, then loop through and assign each
# member to favPenguins, then print as list

penguins = ['rockhopper', 'emperor', 'gentoo', 'king']
for favPenguins in penguins:
    print(favPenguins)

#can enumerate too
for index, favPenguins in enumerate(penguins):
    print (index, favPenguins)

penguins = 'Penguins'
for i in penguins:
    print(i)

# Using range for looping through numbers, range() function has syntax
# range(start, end, stop) although always misses off end

for i in range(2, 12, 3):
    print (i)

    

