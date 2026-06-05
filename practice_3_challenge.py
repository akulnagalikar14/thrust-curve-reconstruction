import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(6, GPIO.OUT)

try:
    while True:
        state = GPIO.input(5)
        time.sleep(0.1)
        stat_after = GPIO.input(5)

        if state != stat_after:
            print(f"GPIO 5 (DT pin) changed from {state} to {stat_after}")
        else:
            continue
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
