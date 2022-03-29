#Sean Kelley
#8 July 2021
#chapter 5 corrected

A_SEAT_PROFIT = 20
B_SEAT_PROFIT = 15
C_SEAT_PROFIT = 10


def calc_profit(a_seats, b_seats, c_seats):
    a_profit = a_seats * A_SEAT_PROFIT #simplified the variables and then added them together under he total_profit variable
    b_profit = b_seats * B_SEAT_PROFIT
    c_profit = c_seats * C_SEAT_PROFIT
    total_profit = a_profit + b_profit + c_profit
    return total_profit


def print_total(total_profit): #no ':'
    print('The total profit is $', format(total_profit, '.2f'), sep = '')


def main():
    print('*** This program determines total profits based on the amount of different seat types sold ***\n')

    section_a_seats = int(input('How many seats were sold in section A? '))
    section_b_seats = int(input('How many seats were sold in section B? '))
    section_c_seats = int(input('How many seats were sold in section C? '))
    profit = calc_profit(section_a_seats, section_b_seats, section_c_seats)
    print_total(profit) #had to add the profit variable


main()