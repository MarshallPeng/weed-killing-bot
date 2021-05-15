import serial
import time
import adafruit_bno055
import adafruit_gps


class GPSSensor:
    def __init__(self):
        self.uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
        self.gps = adafruit_gps.GPS(self.uart, debug=False)
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0") # Turn on the basic GGA and RMC info
        self.gps.send_command(b"PMTK220, 1000")      # Update Rate = 1Hz = 1 sec.

    def get_readings(self):
        self.gps.update()
        if self.gps.has_fix:
            readings = {
                "lat" : self.gps.latitude,
                "long": self.gps.longitude,
                "fix": self.gps.fix_quality
            }
            return readings
        else:
            return None

class IMUSensor:

    def __init__(self):
        self.uart = serial.Serial("/dev/serial0")
        self.sensor = adafruit_bno055.BNO055_I2C(self.uart)

        self.last_val = 0xFFFF

    def _temperature(self):
        result = self.sensor.temperature
        if abs(result - self.last_val) == 128:
            result = self.sensor.temperature
            if abs(result - self.last_val) == 128:
                return 0b00111111 & result
        self.last_val = result
        return result

    def get_readings(self):
        readings = {
            "temp": self._temperature(),
            "accelerometer": self.sensor.acceleration,
            "magnetometer": self.sensor.magnetic,
            "gyroscope": self.sensor.gyro,
            "euler": self.sensor.euler,
            "quaternion": self.sensor.quaternion,
            "lin_accel": self.sensor.linear_acceleration,
            "gravity": self.sensor.gravity
        }
        return readings

class UltrasonicSensor:
    def __init__(self):
        pass
