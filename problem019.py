import argparse
import math

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    args = parser.parse_args()
    
    months = [ 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    year_day = 0  # 1st of January of 1901 was Tuesday
    week_day = 1  # Monday

    sundays = 0
    for year in range(1901, 2001):
        for month in months:
            if month == 0:
                if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
                    month = 29
                else:
                    month = 28
            week_day = (week_day+month)%7
            if week_day == 6:
                sundays += 1
            
    print sundays
