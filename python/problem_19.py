

'''
Project Euler Problem 19

How many Sundays fell o n the first of the month duing the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''


# number of days in each month (non leap year)
months = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

def is_leap_year( year ):
    '''
    Returns true if the given year is a leap year
    '''

    if year % 4 == 0 and not year % 1000 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

    return false


def determine_number_sundays():
    '''
    Determine the number of months started on a Sunday
    '''

    year = 1900
    first_day = 0
    number_of_sundays = 0

    for year in range(1900,2001):
        # determine if its a leap year 
        leap_year = is_leap_year( year )

        for month in months[int(leap_year)]:
            first_day += month % 7
            if first_day > 6:
                first_day -= 7

            if first_day == 6 and year != 1900:
                number_of_sundays += 1

    print 'The number of sundays is ' + str(number_of_sundays)
if __name__ == '__main__':
    # test out leap year
    print is_leap_year( 2000 )
    print is_leap_year( 1996 )
    print is_leap_year( 1997 )
    print is_leap_year( 1998 )

    determine_number_sundays()

    print 31 % 7
