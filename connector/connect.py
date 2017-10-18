import data
import serial
import socket

class SerialConnector:
    @classmethod
    def get(self, arduino_serial):
        return arduino_serial.readline()

    @classmethod
    def get_connection(self):
        return serial.Serial(data.DEVICE_NAME, data.BAUD_RATE)


class UDPConnector:
    @classmethod
    def send(self, value, dstip, dstport, mysocket):
        mysocket.sendto(value, (dstip, dstport))

    @classmethod
    def get_dstip(self):
        return data.IP_ADDRESS

    @classmethod
    def get_dstport(self):
        return data.PORT_NUMBER

    @classmethod
    def make_mysocket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
