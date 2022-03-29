print('Most common character finder')

phrase = input('Enter a phrase: ')

most_common_char = {}

for char in phrase:
    if char in most_common_char:
        most_common_char[char] += 1
    else:
        most_common_char[char] = 1

sorted()
print(most_common_char)
