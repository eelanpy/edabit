# 35_print_date_today:



def date_today(year, month, date):
    months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'Septemeber',10:'October',11:'November',12:'December'}
    if date not in [30,31]:
        print("Yesterday was: {} {} {}".format(months[month],date-1,year))
        print("Today's date is: {} {} {}".format(months[month],date,year))
        print("Tomorrow is: {} {} {}".format(months[month], date+1,year))
    else:
        print("Yesterday was: {} {} {}".format(months[month],date-1,year))
        print("Today's date is: {} {} {}".format(months[month],date,year))
        print("Tomorrow is: {} 1 {}".format(months[month+1],year))

date_today(2020,3,31)






