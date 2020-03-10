for year in range(2000,2101):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(str(year) + " is a leap year")
