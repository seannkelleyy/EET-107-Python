#Sean Kelley
#Ch 9-1
#19 July 2021

print("State Capital's Game")

capitals = {'Ohio': 'Columbus', 'California': 'Sacramento', 'Illinois': 'Springfield', 'Arizona': 'Tuscon',
            'Washington': 'Olympia'}
correct = 0

print('What is the capital of Ohio')
Ohio_input = input('Type your answer: ')
if Ohio_input.title() == capitals["Ohio"]:
    correct += 1
    print('Good Job!')
else:
    print(f'The correct answer is {capitals["Ohio"]}')

print('What is the capital of California')
Cali_input = input('Type your answer: ')
if Cali_input.title() == capitals["California"]:
    correct += 1
    print('Good Job!')
else:
    print(f'The correct answer is {capitals["California"]}')

print('What is the capital of Illinois')
Illinois_input = input('Type your answer: ')
if Illinois_input.title() == capitals["Illinois"]:
    correct += 1
    print('Good Job!')
else:
    print(f'The correct answer is {capitals["Illinois"]}')

print('What is the capital of Arizona')
Arizona_input = input('Type your answer: ')
if Arizona_input.title() == capitals["Arizona"]:
    correct += 1
    print('Good Job!')
else:
    print(f'The correct answer is {capitals["Arizona"]}')

print('What is the capital of Washington')
Washington_input = input('Type your answer: ')
if Washington_input.title() == capitals["Washington"]:
    correct += 1
    print('Good Job!')
else:
    print(f'The correct answer is {capitals["Washington"]}')

print(f'You answered {correct} correctly and {5 - correct} incorrectly')
