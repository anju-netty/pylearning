


#!/usr/bin/python
from string import maketrans

i = 'abcdefghijklmnopqrstuvwxyz'
o = 'cdefghijklmnopqrstuvwxyzab'

transtab = maketrans(i,o)

e = input("Please enter the string to decode it")
print (e.translate(transtab))