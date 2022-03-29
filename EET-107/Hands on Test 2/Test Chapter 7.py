# Sean Kelley
# Test Chapter 7
# 29 July 2021

print('Joe\'s Number Analysis Program.')

total = 0
numbers = []    # the 'numbers variable was not a list
go_on = 'Y'
while go_on.upper() == 'Y':
    number = int(input('\nEnter a number: '))
    numbers.append(number)      # append is a method which means it needs a . not an =
    total += number
    go_on = input('Do you have more numbers to enter? ')

min_number = min(numbers)
max_number = max(numbers)
numbers_entered = len(numbers)
average = total / numbers_entered

print('\nYou entered the values', numbers)
print('A total of', numbers_entered, 'values were entered')
print('The maximum value entered was', max_number)
print('The minimum value entered was', min_number)
print('The average value entered was', format(average, '.2f'))
print('The total of all values entered was', total)