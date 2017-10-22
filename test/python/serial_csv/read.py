import time
import csv
import serial

class Test:
    def __init__(self, arduino_serial):
        self.arduino_serial = arduino_serial

    def main(self):
        data = self.read_data()
        self.write_data(data)

    def read_data(self):
        data = []
        filename = 'test.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f, lineterminator='\n')
            for row in reader:
                data.append(row)
            return data

    def write_data(self, data):
        for row in data:
            for x in range(len(row)):
                self.arduino_serial.write(row[x] + '/')
                time.sleep(0.01)


if __name__ == '__main__':
    arduino_serial = serial.Serial('/dev/cu.usbmodem1421', 9600)
    Test(arduino_serial).main()
