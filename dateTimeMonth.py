import datetime

now = datetime.datetime.now()

# print
# print "Current date and time using str method of datetime object:"
# print str(now)

# print
# print "Current date and time using instance attributes:"
# print "Current year: %d" % now.year
# print "Current month: %d" % now.month
# print "Current day: %d" % now.day
# print "Current hour: %d" % now.hour
# print "Current minute: %d" % now.minute
# print "Current second: %d" % now.second
# print "Current microsecond: %d" % now.microsecond


# hrs =str(now.hour);
# mint =str(now.minute);
# sec  =str(now.second);

# time =hrs+':'+mint+':'+sec
# print
# print "Current date and time using strftime:"
# print time

def getTimeData():
	now = datetime.datetime.now()
	hrs =str(now.hour)
	mint =str(now.minute)
	sec  =str(now.second)
	month = str(now.month)
	date =str(now.day)
	time =hrs+':'+mint+':'+sec
	result = [date,month,time]
	return result


# print
# print "Current date and time using isoformat:"
# print now.isoformat()
