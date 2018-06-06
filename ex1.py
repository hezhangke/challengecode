#!/usr/bin/env python

from string import maketrans
s = raw_input()
upper = []
low = []
for i in range(24):
	low.append(chr(ord('a') + i + 2))
	upper.append(chr(ord('A')+i+2))
for j in range(2):
	low.append(chr(ord('a')+j))
	upper.append(chr(ord('A')+j))
change = ''.join(low+upper)  
upper  = maketrans('','')[65:91]
low = maketrans('','')[97:123]
source = low + upper
print s.translate(maketrans(source,change))

