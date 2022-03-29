#Sean Kelley
#Chapter 9-2
#19 July 2021

print('Unique Word Counter\n')
while True:
    try:
        file_name = input('Please enter the name of the file you wish to process: ')
        words = set(open(file_name).read().split())
        break
    except (FileNotFoundError, OSError):
        print(f'The file {file_name} could not be found')
        print('Enter the file name you wish to process or type exit to quit')
print(len(words))



