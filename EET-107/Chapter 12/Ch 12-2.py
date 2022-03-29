# Sean Kelley
# ch12-2
# 26 July 2021

nested_num_list = (9, 8, 7, 9, 4, 3, 6)

def recursive_min(nested_num_list):
    largest = nested_num_list[0]
    while type(largest) == type([]):
        largest = largest[0]

    for i in nested_num_list:
        if type(i) == type([]):
            min_i = recursive_min(i)
            if largest > min_i:
                largest = min_i
        else:
            if largest > i:
                largest = i

    print(largest)

recursive_min(nested_num_list)
