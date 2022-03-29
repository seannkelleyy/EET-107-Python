#Sean Kelley
#Chapter 6 Lab 1
#5 July 2021

user_file = input("Please enter the name of the file you want to work with: ")
user_cmd = input("Are you going to (r)ead the file of (w)rite the file?: ")


if user_cmd == "w":
   file = open(user_file, 'w')
   f_name = input("Enter your first name: ")
   l_name = input("Enter your last name: ")
   address = input("Enter your address: ")
   city = input("Enter the name of your city: ")
   state = input("Enter the name of your state: ")
   zip = input("Please enter your zip code: ")
   file.write(f_name + ' ')
   file.write(l_name + '\n')
   file.write(address + '\n')
   file.write(city + ', ')
   file.write(state + ' ')
   file.write(zip)
   file.close()
elif user_cmd == "r":
    print("The contents of the file is:")
    file = open(user_file, 'r')
    data = file.read()
    print(data)
    file.close()