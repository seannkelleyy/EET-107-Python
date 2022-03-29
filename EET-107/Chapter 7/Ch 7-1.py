#Sean Kelley
#chapter 7-1
#10 July 2021
import math
from statistics import mean
print('Daily Sales Tracker\n')
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday')
run_count = 0
sales =[]
for day in days:
    if day == [8]:
        break
    s = float(input(f'Enter the sales amount for {days[run_count]}: '))
    sales.append(s)
    run_count += 1
sales_max = max(sales)
sales_min = min(sales)
sales_max_day = sales.index(max(sales))
sales_min_day = sales.index(min(sales))
print(f'Total weekly sales: ${sum(sales)}')
print(f'Average weekly sales: ${round(mean(sales), 2)}\n')
print(f'The highest sale was ${sales_max} on {days[sales_max_day]}')
print(f'The lowest sale was ${sales_min} on {days[sales_min_day]}')
