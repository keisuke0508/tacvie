import data
from connect import *
import make_csv

def main():
    arduino_serial = SerialConnector.get_connection()
    dstip = UDPConnector.get_dstip()
    dstport = UDPConnector.get_dstport()
    mysocket = UDPConnector.make_mysocket()
    csv_data = []
    while True:
        try:
            values = []
            for sensor in range(data.SENSOR_DATA_NUMBER):
                value = SerialConnector.get(arduino_serial)
                UDPConnector.send(value, dstip, dstport, mysocket)
                values.append(value)
            csv_data.append(values)
        except:
            make_csv.CSVMaker().make_csv_test(csv_data)
            break;

if __name__ == "__main__":
    main()
