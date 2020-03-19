# -*- coding: utf-8 -*-

"""
Problem 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Square 	  	P4,n=n2 	  	1, 4, 9, 16, 25, ...
Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

from __future__ import division
from __future__ import print_function
import itertools

MIN, MAX = 10**3, 10**4

figurate_nums = {
			3: lambda n: n*(n+1)//2,
			4: lambda n: n**2,
			5: lambda n: n*(3*n-1)//2,
			6: lambda n: n*(2*n-1),
			7: lambda n: n*(5*n-3)//2,
			8: lambda n: n*(3*n-2)
		}

P = {}
for num, f in figurate_nums.iteritems():
	gen = itertools.imap(f, itertools.count(1))
	gen = itertools.dropwhile(lambda n: n < MIN, gen)
	gen = itertools.takewhile(lambda n: n < MAX, gen)
	P[num] = list(gen)

def check_and_remove(num, l):
	found_in = []
	for i in l:
		if num in P[i]:
			found_in.append(i)
	if len(found_in) == 1:
		l.remove(found_in.pop())
		return True
	return False

def search(numbers, found):
	if not found: return True

	last_two_digit = numbers[-1] % 100
	if last_two_digit < 10: return False
	
	for num in range(last_two_digit * 100, min(last_two_digit * 100 + 100, MAX)):
		tmp = found[:]
		if check_and_remove(num, found): 
			numbers.append(num)
			if search(numbers, found):
				break
			else:
				numbers.pop(-1)
				found = tmp
	else:
		return False
	
	return True
	
results = []
for num in range(MIN, MAX):
	found = figurate_nums.keys()
	if check_and_remove(num, found):
		numbers = [num]
		if search(numbers, found):
			results.append(numbers[:])

for numbers in results:
	if str(numbers[-1])[-2:] == str(numbers[0])[:2]:
		print(numbers, "Sum =", sum(numbers))