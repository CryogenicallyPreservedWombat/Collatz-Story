import re
from random import randint, random

# Returns inputted station number
def run_intro(minute, hour):
    intro = open('intro.txt', mode='r').read()
    intro = intro.replace('(TIME)', '{}:{}'.format(hour, minute if minute >= 10 else '0' + str(minute)))
    station = input(intro)
    return station

def invalid_station(station_str):
    sorry = open('sorry.txt', mode='r').read()
    sorry = sorry.replace('(STATION)', station_str)
    return input(sorry)
    
# Returns whether or not station input was success
def run_response(station_str):

    station_str = station_str.lower().replace('station', '')

    try:
        station_num = int(station_str)
        assert(station_num > 0)
        return station_num 
    except:
        return run_response(invalid_station(station_str))

def update_time(minute, hour):
    minute += randint(2, 13)
    hour += minute // 60

    minute %= 60
    hour = (hour - 1) % 12 + 1
    return minute, hour

def collatz_step(num):
    return int(num / 2 if num % 2 == 0 else num * 3 + 1)

def the_whole_shebang(minute=55, hour=11):
    next_station = 0
    while True:
        station_num = run_response(run_intro(minute, hour))
        if station_num != next_station and next_station:
            confirm = open('confirmation.txt', 'r').read()
            yes_no = input(confirm.replace('(STATION)', str(station_num))).lower()
            ans = False
            while not ans:
                # maybe drop whitespace later
                if 'yes' == yes_no:
                    ans = True
                elif 'no' == yes_no:
                    no = open('no.txt', 'r').read()
                    station_num = run_response(input(no))
                    ans = True
                else:
                    shiver = open('shiver.txt', 'r').read()
                    yes_no = input(shiver)
    
        
        next_station = collatz_step(station_num)
        minute, hour = update_time(minute, hour)

        finale = open('finale.txt', mode='r').read()
        finale = finale.replace('(TIME)', '{}:{}'.format(hour, minute if minute > 10 else '0' + str(minute)))
        finale = finale.replace('(STATION)', '{}'.format(next_station))
        print(finale)

        if next_station == 1 and random() > 0.75:
            start_again = open('exit.txt', mode='r').read()
            start_again = start_again.replace('(MINUTE)', str(randint(31, 47)))
            print(start_again)

            # Resetting to defaults

            next_station = 0
            hour = 11
            minute = 45

the_whole_shebang()
