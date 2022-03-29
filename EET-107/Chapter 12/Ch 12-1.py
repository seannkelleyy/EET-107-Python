# Sean Kelley
# ch12-1
# 26 July 2021
character = input('What character would you like to repeat?: ')

times = int(input(f'How many {character} would you like?: '))


def character_generation(character, times):
        print(character * times)


character_generation(character, times)
