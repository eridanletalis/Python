from _datetime import date, timedelta
input_date = date(*(i for i in [int(i) for i in input().split()]))
input_days = timedelta(days=int(input()))
result_date = input_date + input_days
print(result_date.year, result_date.month, result_date.day)
