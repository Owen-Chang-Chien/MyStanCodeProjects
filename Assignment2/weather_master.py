"""
File: weather_master.py
Name:Owen Zhangjian
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	When a user inputs weather data, this program tells the user the highest temperature and the lowest one. Also, this
	program can tell the average and the cold days among these data. If the user inputs -100, the program will tell all
	the information mentioned above. Honestly, my program only told the cold days and the highest temperature. I tried to
	finish assignment 2 all by myself, but I failed. I didn't know how to calculate the average.
	"""
	print('stanCode \"Weather Master 4.0"!')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	a = 0  # I use this variable to calculate the number of cold days.
	if data == -100:  # Sentinel value
		print('No temperatures were entered.')
	else:
		maximum = data
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == EXIT:
				break
			else:
				if data < 16:
					a += 1
				if data > maximum:
					maximum = data
				if data < 0:
					minimum = data
					if data < minimum:
						minimum = data

		print('Highest Temperature = ' + str(maximum))
		print('Lowest Temperature = ' )
		print('Average = ')
		print(str(a) + ' cold day(s)')


def the_smallest():
	data = int(input('Next Temperature: (or -100 to quit)? '))

















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
