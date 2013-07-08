#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

	Copyright 2013 Florian Jacob
"""

try:
	from scriptine import run, path, log
	from scriptine import shell
except ImportError:
	print("You need to install python-scriptine to run mezamashi.")
	sys.exit(1)

import time
from datetime import datetime, timedelta, date
import re
import sys

WAKE_COMMAND = "<your musicplayer with song here>"

absolute_time = re.compile("[0-2]?[0-9]:[0-5][0-9]")
relative_time = re.compile("[0-9]?[0-9]h([0-5][0-9])?")

def parsetime(timestr):
	timestr = timestr.strip()
	now_timestamp = time.time()
	result_timestamp = now_timestamp
	if timestr == "now":
		pass
	elif relative_time.match(timestr):
		splitted = timestr.split("h")
		hours = int(splitted[0])
		minutes = int(splitted[1]) if splitted[1] != '' else 0

		result_timestamp += hours * 60 * 60 + minutes * 60

	elif absolute_time.match(timestr):
		current_datetime = datetime.now()
		today = date.today()
		result_datetime = datetime(today.year, today.month, today.day)

		splitted = timestr.split(":")
		hour = int(splitted[0])
		minute = int(splitted[1]) if splitted[1] != '' else 0

		if current_datetime.hour < hour or (current_datetime.hour == hour and current_datetime.minute < minute):
			# the absolute time given will be reached today
			result_datetime += timedelta(hours=hour, minutes=minute)
		else:
			# the absolute time given will be reached tomorrow
			result_datetime += timedelta(days=1, hours=hour, minutes=minute)
		result_timestamp = time.mktime(result_datetime.timetuple())
	else:
		print("{} can't be parsed as relative or absolute time." % timestr)
		sys.exit(1)
	return result_timestamp


def set_command(alarm_time):
	"""
	set the alarm time.
	:param time: the time to wake up, either absolute as "8:00" or relative as "8h00"
	"""
	alarm_timestamp = parsetime(alarm_time)
	print(datetime.fromtimestamp(alarm_timestamp))
	shell.call(['sudo', 'rtcwake', '-l', '-m', 'no', '-t', str(int(alarm_timestamp))])

def sleep_command(sleep_time):
	"""
	set the time to suspend the computer
	:param sleeptime: the time to sleep, either absolute as "23:00" or relative as "1h00" or "now"
	"""
	now_timestamp = time.time()
	sleep_timestamp = parsetime(sleep_time)
	print(datetime.fromtimestamp(sleep_timestamp))
	time.sleep(sleep_timestamp - now_timestamp)
	shell.sh("systemctl suspend")
	shell.sh(WAKE_COMMAND)


def unset_command():
	"""
	unset the current alarm
	"""
	shell.sh("sudo rtcwake -l -m disable")

def show_command():
	"""
	show the current alarm time
	"""
	shell.sh("sudo rtcwake -l -m show")

if __name__ == '__main__':
    run()
