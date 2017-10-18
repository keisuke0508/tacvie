import data
from connect import *

def main():
    arduino_serial = SerialConnector.get_connection()
    dstip = UDPConnector.get_dstip()
    dstport = UDPConnector.get_dstport()
    mysocket = UDPConnector.make_mysocket()
    while True:
        try:
            value = SerialConnector.get(arduino_serial)
            UDPConnector.send(value, dstip, dstport, mysocket)
        except:
            break;

if __name__ == "__main__":
    main()
