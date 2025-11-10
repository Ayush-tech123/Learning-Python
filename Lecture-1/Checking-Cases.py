#strings

import platform
name = "ayush"

print(name.upper().isupper())
print(name.lower().isupper())
print(name.upper().islower())
print(name.lower().islower())

#Finding length of a string

print(len(name))

line = "Writing a line to see how the len function works"

print(len(line))

#Printing a character from a work or line

print(name[0])
print(name[1])
print(name[2])
print(line[18])
print(line[22])

#Checking Index from name or line

print(name.index('s'))
print(line.index('o'))

#Replacing alphhabets in whole sentence or paragraph

print(name.replace('a','s'))