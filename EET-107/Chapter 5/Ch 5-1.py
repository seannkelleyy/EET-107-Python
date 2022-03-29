#Sean Kelley
#Lab 5.1
#29 June 2021

while True: #this while loop checks to make sure a valid input is entered
        try:
            temp = float(input("Please enter the current temperature: "))
            break
        except:
            print("Invalid input")
while True:  #this while loop checks to make sure a valid input is entered
        try:
            temp_unit = input("Did you enter the temperature in (c)elcius or (f)ahrenheit?: ")
            break
        except:
            print("Invalid input")
if temp_unit == 'c': #this if and elif statement converts the unit entered to its full word
    temp_unit = 'Celcius'

elif temp_unit == 'f':
    temp_unit = 'Fahrenheit'
other_unit = 0

if temp_unit == 'Celcius':  #this if statement makes a variable that is the opposite of the entered unit
    other_unit = 'Fahrenheit'

elif temp_unit == 'Fahrenheit':
    other_unit = 'Celcius'

temp_conv = 0
if temp_unit == 'Celcius': #this if statement converts the temperature to the other unit
    temp_conv = (temp) * (9/5) + 32
elif temp_unit =='Fahrenheit':
    temp_conv = (temp) / (9/5) +32

print(f"The current temperature is {temp} degrees {temp_unit}, this temperature in {other_unit} is {temp_conv}")