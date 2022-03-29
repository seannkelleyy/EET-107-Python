#Sean Kelley Chapter 3 Lab 1 18 June 2021
print("Numeric Workday Translator")
print()
work_day_num = int(input("Enter a numeric value of a workday that you wish to translate: "))
work_day = ["Weekend", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if work_day_num < 6:
    print("The Workday is " + work_day[work_day_num])
else:
    print("This Number Is Not Valid")
