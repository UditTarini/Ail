import datetime
import os
import time
import random
from os import listdir
from os.path import isfile, join
import playsound
import main

def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False


def playAlarm():
    # Get user input for the alarm time
    main.ail('set alarm time')
    print("It should be in HH:MM or HH:MM:SS format (Ex. 06:30 or 18:30:00)")
    while True:
        alarm_input = input(">> ")
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")

    # Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])


    # Get the current time of day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

    time_diff_seconds = alarm_seconds - current_time_seconds

    if time_diff_seconds < 0:
        time_diff_seconds += 86400  # number of seconds in a day

    # Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)

    # Time for the alarm to go off
    print("Wake Up!")

    # Load list of possible songs
    mypath='alarm'
    soundList = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    sound=random.choice(soundList)
    path='alarm\\'+sound

    playsound.playsound(path, True)


