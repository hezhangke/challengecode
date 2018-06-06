#!/usr/bin/env python

from string import maketrans
s = raw_input()
upper = []
low = []
for i in range(24):
	low.append(chr(ord('a') + i + 2))

