#Parker Reece
#Calculating hours per week

print('Easy way to calculate how many hours per week need')
from datetime import datetime

print'\n'
mon = input('How many hours on Monday? ')
print'\n'
tues = input('How many hours on Tuesday? ')
print'\n'
wed = input('How many hours on Wednesday? ')
print'\n'
thurs = input('How many hours on Thursday? ')
print'\n'

#Adding hours
total = mon + tues + wed + thurs
to_go = 40 - total
    
#Determine what day it is
if tues == 0:
	day = 'Tuesday'
	per_day = to_go/4
elif wed == 0:
	day = 'Wednesday'
	per_day = to_go/3
elif thurs == 0:
	day = 'Thursday'
	per_day = to_go/2
else: 
	day = 'Friday'
	per_day = to_go

#Resulting output   
print "********  It\'s " '%s' " ********" %(day)
print'\n'
print(round(to_go,2), 'Hours left to go')
print(round(per_day,2), 'Hours per day')
print'\n'

if day == 'Friday':
    so_far = input('How many hours worked today? ')
    print'\n'
    more_today = abs(to_go-so_far) 
    print round(more_today,2), 'more hours today'
    print'\n'
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    if minute > 60:
	minute -= 60
    if hour > 12:
        hour -=  12
    print "Right now, its " '%s:%s' %(hour, minute)
    print'\n'
    end_time_m = (more_today - int(round(more_today,0)))* 60 + int(round(now.minute))
    end_time_h = int(round(more_today,0)) + hour
    print "If you work until " '%s:%s' ' you can hit 40 hours.' %(end_time_h, int(end_time_m))
    print'\n'
    end_the_week = 40 - more_today
    lost_money = more_today * 25
    print "Or stop now and end the week with " '%s' " and loose about $" '%s' " without taxes." %(end_the_week, lost_money)
    print'\n'
