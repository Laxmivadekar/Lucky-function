month_days=[0,31,28,31,30,31,30,31,30,31,30,31]
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)
def day_in_month(year,month):
    if not 1>=month<=12:
        return 'invalid month'
    if month==2 and is_leap(year):
        return "29"
    return month_days[month]
print(is_leap(2017))
print(is_leap(2020))
print(day_in_month(2019,1))
