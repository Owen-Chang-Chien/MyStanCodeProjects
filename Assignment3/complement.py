"""
File: complement.py
Name: Owen Zhangjian
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    I finished this program thanks to the discussion with  my TA HuaJung Chang.

    This main function asks users to input a DNA sequence composed of A(Adenine), T (Thymine), C (Cytosine)
    , and G (Guanine) only. Then, this function will tell users the complementary DNA sequence of the input.
    """
    s = input("Please give me a DNA strand and I'll find the complement: ")
    s = s.upper()   # case-insensitive
    build_complement(s)
    print('The complement of ' + str(s) + ' is ' + str(build_complement(s)))


def build_complement(s):
    """
    This function helps change an input DNA sequence into its complementary DNA sequence.
    """
    dna = ''
    for i in range(len(s)):
        complement = s[i]
        if complement == 'A':
            dna = dna + 'T'
        if complement == 'T':
            dna = dna + 'A'
        if complement == 'C':
            dna = dna + 'G'
        if complement == 'G':
            dna = dna + 'C'
    return dna


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
