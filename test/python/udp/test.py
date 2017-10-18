import socket
import time

class Test:
    def __init__(self, dstip, dstport):
        self.dstip = dstip
        self.dstport = dstport

    def main(self):
        data = self.getData()
        self.sendData(data, 'success')

    def getData(self):
        data = []
        for x in range(100):
            data.append(str(x))
        return data

    def sendData(self, data, message):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for x in range(len(data)):
            mysocket.sendto(data[x], (self.dstip, self.dstport))
            time.sleep(0.1)
        mysocket.sendto(message, (self.dstip, self.dstport))

if __name__ == '__main__':
    dstip = "192.168.1.4"
    dstport = 8000
    Test(dstip, dstport).main()
