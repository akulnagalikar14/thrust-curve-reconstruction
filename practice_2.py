import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 50)

pwm.start(0)

range = [2,5,7,10,12]

for duty in range:
    pwm.ChangeDutyCycle(duty)
    print(f"Duty Cycle: {duty}%")
    time.sleep(1)

pwm.stop()
GPIO.cleanup()