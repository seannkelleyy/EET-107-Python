#Sean Kelley
#ch8-1
#15 July 2021

print('Name Processor')

name = input('Enter your name: ')
capital_name = name.title()
if name.count(',') > 0:
    print(capital_name)
else:
    split_name2 = capital_name.split(' ')
    print(f'{split_name2[-1]}, {split_name2[0]}')