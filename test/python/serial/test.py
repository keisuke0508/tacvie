import serial

class Test:
    def __init__(self, arduino_serial):
        self.arduino_serial = arduino_serial

    def main(self):
        while True:
            try:
                print self.arduino_serial.readline()
            except:
                break

if __name__ == '__main__':
    arduino_serial = serial.Serial('/dev/cu.usbmodem1421', 9600)
    Test(arduino_serial).main()
