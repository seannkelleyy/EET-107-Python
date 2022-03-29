#Sean Kelley
#8 July 2021
#Chapter 4 corrected

CALORIES_PER_MILE_PER_POUND = 1
max = int(input('What is the maximum number of miles you might run? '))
weight = float(input('How much do you weigh? '))
for current_mileage in range(max): # no ':'
    calories_burnt = (current_mileage + 1) * weight * CALORIES_PER_MILE_PER_POUND #I addded the '+1' to this line as well so it displays the correct number of miles.
    print('After', (current_mileage + 1), 'mile(s) you will have burnt', calories_burnt, 'calories') #no indent to put the print statement in the for loop

