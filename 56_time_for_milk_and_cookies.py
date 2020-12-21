# 56_time_for_milk_cookies:

def time_for_milk_and_cookies(month, date, year):
    if date == 24:
        print('True')
    else:
        print('People do not put cookies on {} {}. '.format(month.title(), date))

time_for_milk_and_cookies('December', 25,2020)