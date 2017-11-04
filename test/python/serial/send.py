import sys, serial, time, random

class Test:
    def __init__(self):
        self.arduino_serial = self.set_serial()

    def main(self):
        angles = self.get_angles()
        while True:
            # while self.arduino_serial.inWaiting() > 0:
            #     self.write_angle(str(random.randint(0, 90)))
            # try:
            #     self.write_angle(str(random.randint(0, 90)))
            # except KeyboardInterrupt:
            #     sys.exit()
            # except:
            #     pass
            for angle in angles:
                self.write_angle(angle)
            for angle in reversed(angles):
                self.write_angle(angle)

    def write_angle(self, angle):
        self.arduino_serial.write(angle + '/')
        print angle
        time.sleep(0.01)

    def get_angles(self):
        return map(str, [i for i in range(91)])

    def set_serial(self):
        return serial.Serial(self.get_device_name(), self.get_baud_rate())

    def get_device_name(self):
        return "/dev/cu.usbmodem1421"

    def get_baud_rate(self):
        return 9600


if __name__ == '__main__':
    Test().main()
