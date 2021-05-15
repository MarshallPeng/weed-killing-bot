import RPi.GPIO as GPIO


class DriveTrain:

    def __init__(self):
        self.motor1_dir = 16
        self.motor1_pwm = 12
        self.motor2_dir = 6
        self.motor2_pwm = 13

        GPIO.setup(self.motor1_dir, GPIO.OUT)
        GPIO.setup(self.motor1_pwm, GPIO.OUT)
        GPIO.setup(self.motor2_dir, GPIO.OUT)
        GPIO.setup(self.motor2_pwm, GPIO.OUT)

        self.power1 = GPIO.PWM(self.motor1_pwm, 1000)
        self.power2 = GPIO.PWM(self.motor2_pwm, 1000)
        
        self.drive_speed = 75

    def forwards(self):
        GPIO.output(self.motor1_dir, GPIO.LOW)
        GPIO.output(self.motor2_dir, GPIO.HIGH)
        self.power1.start(self.drive_speed)
        self.power2.start(self.drive_speed)

    def backwards(self):
        GPIO.output(self.motor1_dir, GPIO.HIGH)
        GPIO.output(self.motor2_dir, GPIO.LOW)
        self.power1.start(self.drive_speed)
        self.power2.start(self.drive_speed)

    def left(self):
        GPIO.output(self.motor1_dir, GPIO.LOW)
        GPIO.output(self.motor2_dir, GPIO.LOW)
        self.power1.start(self.drive_speed)
        self.power2.start(self.drive_speed)

    def right(self):
        GPIO.output(self.motor1_dir, GPIO.HIGH)
        GPIO.output(self.motor2_dir, GPIO.HIGH)
        self.power1.start(self.drive_speed)
        self.power2.start(self.drive_speed)

    def stop(self):
        self.power1.start(0)
        self.power2.start(0)
