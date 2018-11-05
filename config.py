import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
PIN = 10                       # Pin to which the PowerSwitch Tail is connected
ALARM_DURATION = 15            # Light duration in minutes

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = True
BASIC_AUTH_USERNAME = 'ISTC'
BASIC_AUTH_PASSWORD = '00000000'

# -- Custom Happy Messages
MESSAGES = [
    "This Clock is really SECURITY!",
    "You're just a Script KIDDIE!"
]
