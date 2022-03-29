# Sean Kelley
# Test chapter 10
# 27 July 2021

class Pet:  # had to change 'def' to 'class'
    def __init__(self, n, t, a):
        self.__name = n
        self.__type = t
        self.__age = a

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def get_type(self):
        return self.__type

    def set_type(self, t):
        self.__type = t

    def get_age(self):
        return self.__age

    def set_age(self, a):
        self.__age = a     # had to change 'age' to 'a'

    def __str__(self):
        return 'name: ' + self.get_name() + '\n' + \
               'type: ' + self.get_type() + '\n' + \
               'age : ' + str(self.get_age())


def main():
    the_pet = Pet('none', '?', 0)

    changes_needed = True
    while changes_needed:
        print('Current pet data\n\n', the_pet, sep='')
        change_type = input('\nWould you like to change the (n)ame, (t)ype, (a)ge or e(x)it? ')
        if change_type.lower() == 'x':
            changes_needed = False
        elif change_type.lower() == 'n':
            new_info = input('What is the name of the pet? ')
            the_pet.set_name(new_info)     # had to add 'the_pet." in front of the set_name
        elif change_type.lower() == 't':
            new_info = input('What type of pet is it? ')
            the_pet.set_type(new_info)
        elif change_type.lower() == 'a':
            new_info = int(input('How old is the pet? '))
            the_pet.set_age(new_info)

    print('\nFinal pet data\n\n', the_pet, sep='')


main()
