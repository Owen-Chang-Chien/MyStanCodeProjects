"""
File: hailstone.py
Name:Owen Zhangjian
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program is designed to simulate the Hailstone sequence, defined by Douglas Hofstadter. When using this program,
    users should input a natural number first. The execution of this sequence will continue until the number reaches 1.
    In the end, this program will tell users how many steps it will take from the input to one.
    """

    print('This program computes Hailstone sequence.')
    print('')
    a = 0  # This variable is introduced to calculate the steps.
    n = int(input('Enter a number: '))
    if n == 1:  # Sentinel value
        print('It took 0 steps to reach 1.')
    else:
        while True:
            if n % 2 == 1:
                print(str(n)+' is odd, so I make 3n+1: '+str(3*n+1))
                n = 3*n+1
                a += 1

            if n % 2 == 0:
                print(str(n)+' is even, so I take half: '+str(int(float(n/2))))
                n = int(float(n/2))
                a += 1

            if n == 1:
                print('It took '+str(a) + ' steps to reach 1.')
                break


# DO NOT EDIT CODE BELOW THIS LINE

if __name__ == "__main__":
    main()
