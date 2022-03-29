# Lab 3.2
# June 19,2021
# Sean Kelley
BASE_RATE = 50
print('Car Insurance Rate Estimator') # the "/n" was not needed
age = int(input('Enter your current age: '))
sex = input('Enter your sex (M or F): ') #added the M or F to specify how to enter the sex
state = input('Enter your state of residence (Ex: OH): ') #added an example to give correct format to user
if(sex == 'M'):  #added an extra "=" because one "=" does not compare
    sex_premium = BASE_RATE * .25
else: sex_premium = 0
if(state == 'MI' or state == 'FL'):
    state_premium = BASE_RATE * .10
else:
    state_premium = 0
if(age < 21 or age > 70):
    age_premium = BASE_RATE * .05
else: age_premium = 0  #added indents and else statements because having the same variable in multiple if statements did not seem to work
print('\nYou are a', age, 'year old ', sex, 'and you live in ', state) #stateofresidence was not defined
print('Your insurance will cost $', format(BASE_RATE + sex_premium + state_premium + age_premium, '.2f'), sep='')
#I made an addition of all the variables from the if statements