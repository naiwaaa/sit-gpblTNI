#!/usr/bin/env python3
import socket

# import time

# import RPi.GPIO as GPIO
from modules import Listener, Speaker

# emergency_button = 10

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(emergency_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

HOST = ""  # "192.168.43.86"
PORT = 65432

if __name__ == "__main__":
    listener = Listener()
    speaker = Speaker()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            # if GPIO.input(emergency_button) == GPIO.HIGH:
            #     speaker.speak_g("I called an ambulance. Ambulance will be here soon.")
            #     time.sleep(1)
            # else:
            command = listener.listen_from_mic()
            if command == "" or "<timeout>" in command:
                continue
            elif "<unknownvalue>" in command or "<???>" in command:
                speaker.speak("Sorry, I did not catch your words.")
            else:
                s.sendall(command.encode())
                answer = s.recv(1024).decode()
                if answer != "":
                    speaker.speak(answer)
