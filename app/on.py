#!/usr/bin/env python
from light_driver import LightDriver
from playsound import playsound

def main():
    driver = LightDriver()
    driver.on()
    playsound('/opt/pi_alarm_env/pi_alarm/app/laugh.mp3')

if __name__ == "__main__":
	main()
