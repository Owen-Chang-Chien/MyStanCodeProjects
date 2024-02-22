"""
File: prime_checker.py
Name:Owen Zhangjian
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


EXIT = -1


def main():
	"""
	Users could check whether an integer is a prime number or not continually by using this program. If a user enter the
	number -1, this program will stop and tell the user ' Have a good one!'. I tried to categorize all integers, but I failed.
	"""
	print('Welcome to the prime checker!')
	a = 2  # the smallest prime number
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break

		if n == 2:
			print('2 is a prime number!')

		if n != a and n % a == 0:
			print(str(n) + ' is not a prime number!')

		if n % 5 == 0:
			print(str(n) + ' is not a prime number!')

		if n % a == 1:































# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
