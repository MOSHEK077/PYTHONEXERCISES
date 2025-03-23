"""
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600 
    seconds %= 3600
    minutes = seconds // 60 
    seconds %= 60
    return "%d:%02d:%02d" % (hour,minutes,seconds)
n = 1231
print(convert(n))"""


import datetime
def convert(n):
    return str(datetime.timedelta(seconds=n))
#driver programm
n =131413
print(convert(n))