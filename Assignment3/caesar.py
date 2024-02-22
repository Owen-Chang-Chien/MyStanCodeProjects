"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    I finished this program thanks to the discussion with  my TA HuaJung Chang.

    This program demonstrates the process of caesar cipher. Users could change the order of an alphabetic sequence into
    a new alphabetic order by inputting secret number. Then, users are asked to input their ciphered string, and
    the program will decipher the string.
    """
    secret_number = int(input('Secret number: '))
    first_half = ALPHABET[26 - secret_number:26]
    second_half = ALPHABET[0:26 - secret_number]
    new_alphabet = first_half + second_half  # a shifted new alphabetic number.

    cipher = input("What's the ciphered string?")
    cipher = cipher.upper()  # case insensitive
    for i in range(len(cipher)):

        decipher = ''
        if cipher[i].isalpha():
            count = new_alphabet.find(cipher[i])
            decipher += ALPHABET[count]
            print(decipher, end='')

        else:
            decipher += cipher[i]
            print(decipher, end='')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
