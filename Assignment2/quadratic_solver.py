"""
File: quadratic_solver.py
Name:Owen Zhangjian
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program is designed to solve a quadratic equation. The standard form of a quadratic equation is
	ax^2 + bx + c = 0. Users should input a, b, and c. Then this program will tell users the solutions of the equation
	in floating-point number by calculating the discriminant, which equals to b^2-4ac.
	"""

	print('stanCode Quadratic Solver!')
	a = int(input('Please enter the leading coefficient: '))
	b = int(input('Please enter the second coefficient: '))
	c = int(input('Please enter the constant term: '))
	d = b**2 - 4*a*c  # the discriminant

	if d < 0:
		print('No real roots.')
	else:
		y = math.sqrt(d)
		x1 = float((-b+y)/(2*a))
		x2 = float((-b-y)/(2*a))
		if d > 0:
			print('Two roots: '+str(x1)+' , '+str(x2))
		elif d == 0:
			print('One root: '+str(x1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
