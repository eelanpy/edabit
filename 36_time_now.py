#36_time_now:

def time_now(hour, minute):
    time = ''
    if hour in [1,2,3,4,5,6,7,8,9]:
        time += '0{}:'.format(hour)
    if minute in [1,2,3,4,5,6,7,8,9]:
        time += '{}:0{}'.format(hour,minute)
    if minute == 60 or minute == 0:
        time = '{}:00'.format(hour)

    print(time)

time_now(12,7)