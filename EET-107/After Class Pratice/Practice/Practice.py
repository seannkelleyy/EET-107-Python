input_numbers = 4, 2, 1, 5
number_array = []


def solution(A):
    for n in A:
        number_array.append(n)
        number_array.sort()
        for number in range(0, 10):
            number_array.count(number)
            if number == 0:
                return number
    print(number)


solution(input_numbers)