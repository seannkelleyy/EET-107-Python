# Sean Kelley
# Test chapter 8
# 29 July 2021

def main():
    print('Vowel and Consonants Counter\n')
    string_to_process = input('Enter any phrase: ')
    print('The phrase "', string_to_process, '" contains ',
        find_vowels(string_to_process),
        ' vowels and ', find_consonants(string_to_process),
        ' consonants.', sep = '')


def find_vowels(phrase):
    vowels = 0
    for letter in phrase:
        if letter.lower() in ('a', 'i', 'o', 'u', 'e'):     # had to add a space after the commas and add an e.
            vowels += 1    # had to add a '+' in front of the '=' so it adds to the list instead of always being 1
    return vowels


def find_consonants(phrase):    # had to add ':' at the end
    consonants = 0
    vowels = "aeiou"
    for letter in phrase:
        if letter.isalnum():
            if letter.lower() not in vowels:
                consonants += 1
    return consonants


main()
