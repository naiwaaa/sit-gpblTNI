import wiringpi
import time

button_pin = 15
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(button_pin, 0)
wiringpi.pullUpDnControl(button_pin, 1)

while True:
    if wiringpi.digitalRead(button_pin) == 0:
        print("Switch OFF")
    else:
        print("Emergency")
    time.sleep(0.7)
