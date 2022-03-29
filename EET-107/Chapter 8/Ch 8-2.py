#Sean Kelley
#Ch8-2
#16 July 2021

print('File Processor\n')
file = input('Enter the name of the file you want to open: ')
o = open(file, 'rt')
f = o.read()
words = f.split(' ')
count=`0`
for i in f:
    if i.isupper():
        count=count+1
print(f'The file {file} contains {len(words)} words and {count} capital letters')