import serial
import socket

class Test:
    def __init__(self, arduino_serial, dstip, dstport):
        self.arduino_serial = arduino_serial
        self.dstip = dstip
        self.dstport = dstport

    def main(self):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                data = self.getData()
                self.sendData(mysocket, data)
            except:
                break

    def getData(self):
        return self.arduino_serial.readline()

    def sendData(self, mysocket, data):
        mysocket.sendto(data, (self.dstip, self.dstport))

if __name__ == '__main__':
    arduino_serial = serial.Serial('/dev/cu.usbmodem1421', 9600)
    dstip = "192.168.1.4"
    dstport = 8000
    Test(arduino_serial, dstip, dstport).main()
