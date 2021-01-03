from browser import document, timer
import datetime


def time():
	now = datetime.datetime.now()
	hours = now.hour if now.hour >= 10 else '0' + str(now.hour)
	minutes = now.minute if now.minute >= 10 else '0' + str(now.minute)
	seconds = now.second if now.second >= 10 else '0' + str(now.second)
	document.getElementById('time').text = f'{hours}:{minutes}:{seconds}'


timer.set_interval(time, 1000)
