import constant
from connect import *
import data

def main():
    arduino_serial = SerialConnector.get_connection()
    dstip = UDPConnector.get_dstip()
    dstport = UDPConnector.get_dstport()
    mysocket = UDPConnector.make_mysocket()
    csv_data = []
    while True:
        try:
            values = []
            for sensor in range(constant.SENSOR_DATA_NUMBER):
                value = SerialConnector.receive(arduino_serial)
                UDPConnector.send(value, dstip, dstport, mysocket)
                values.append(value)
            csv_data.append(values)
        except:
            data.CSVMaker().make_csv_test(csv_data)
            break;

if __name__ == "__main__":
    main()
