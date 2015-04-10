import string
from datetime import date, time, datetime

def getdayoftheweek(dt):
	
	try:
		dt = date(2014,01,40)
		day = dt.isoweekday()
		if day == 1:
			return 'Monday'
		elif day == 2:
			return 'Tuesday'
		elif day == 3:
			return 'Wednesday'
		elif day == 4:
			return 'Thursday'
		elif day == 5:
			return 'Friday'
		elif day == 6:
			return 'Saturday'
		elif day == 7:
			return 'Sunday'
		else:
			return 'Invalid Date'
	except:
		print "Damn it is working"
		#raise
	else:
		return 'tutu'
		
#dt = date.today()
#dt = date(2014,01,31)
#print getdayoftheweek(dt)


def calculateage(dt):
	today = date.today()
	bday = dt.replace(year = today.year)
	if bday < today:
		bday = bday.replace(year = today.year + 1)
	datetimenow  = datetime.now()
	datetimebday = datetime(bday.year, bday.month, bday.day)
	tdelta = abs(datetimebday - datetimenow)
	min, sec = divmod(tdelta.seconds, 60)
	hr, min = divmod(min, 60)
	return (tdelta.days, hr, min, sec)
	
	
	
	
	
dt = date(1983,8,21)
print calculateage(dt)
	
	
key = 5fca88677185ab39

'http://api.wunderground.com/api/5fca88677185ab39/conditions/q/autoip.json?geo_ip=116.88.249.30
        

http://api.wunderground.com/api/5fca88677185ab39/conditions/q/CA/San_Francisco.json
	
	
	
	
	
	
	
	
	
	
	
	
	





