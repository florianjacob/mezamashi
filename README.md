# mezamashi - めざまし #
## terminal alarm clock written in python ##

Commands:
```
Usage: mezamashi.py command [options]

Options:
  -h, --help  show this help message and exit

Commands:
  show   show the current alarm time
  sleep  set the time to suspend the computer
  set    set the alarm time.
  unset  unset the current alarm
```

Example usage:
```
# set a wakeup alarm to 8 o'clock
>./mezamashi.py set 8:00
# show the current alarm
>./mezamashi.py show
# disable the current alarm
>./mezamashi.py unset
# set a wakeup alarm in 7 hours and a half
>./mezamashi.py set 7h30
# go to sleep in 20 minutes. you need to use this command to suspend to run the WAKEUP_COMMAND at next startup
>./mezamashi.py sleep 
```

mezamashi expects rtcwake, systemd (for systemctl suspend) and sudo to be installed on the system.

mezamashi uses the scriptine python module for command parsing and execution, make sure it's installed with
```
sudo pip install scriptine
```
or
```
sudo easy_install scriptine
```

## Licensing ##
mezamashi is licensed under the General Public License version 3,
the text of which can be found in LICENSE, or any later version of the GPL,
unless otherwise noted.

Licensing of used libraries:
	* python: PSFL
	* scriptine: MIT

## Attribution ##
mezamashi is written by Florian Jacob.
