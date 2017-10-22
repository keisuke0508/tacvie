import serial
import csv

class Test:
    def __init__(self, arduino_serial):
        self.arduino_serial = arduino_serial

    def main(self):
        data = self.getData()
        self.writeData(data)
        print data

    def getData(self):
        data = []
        while True:
            try:
                factor = []
                for x in range(3):
                    factor.append(int(self.arduino_serial.readline()))
                data.append(factor)
            except:
                break
        return data

    def writeData(self, data):
        csv_file = open('test.csv', 'w')
        csv_writer = csv.writer(csv_file, lineterminator='\n')
        csv_writer.writerows(data)
        csv_file.close()


if __name__ == '__main__':
    arduino_serial = serial.Serial('/dev/cu.usbmodem1421', 9600)
    Test(arduino_serial).main()
