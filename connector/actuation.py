import cv2
import time
import sys
import constant
from connect import *
import data

def main_senbay_ver():
    mysocket = SensorDataReceiver.make_mysocket()
    SensorDataReceiver.bind_mysocket(mysocket)
    arduino_serial = SerialConnector.get_connection()
    while True:
        try:
            sensor_data = SensorDataReceiver.receive_sensor_data(mysocket)
            arduino_serial.write(sensor_data + '/')
            print sensor_data
        except KeyboardInterrupt:
            sys.exit()
        except:
            arduino_serial.write('48.13/')

def main_csv_ver():
    value_number = 0
    # video = data.VideoPlayer.get_video()
    # csv_data = data.CSVReader().read_csv()
    video = data.VideoPlayer.get_video_test()
    csv_data = data.CSVReader().read_csv_test()
    arduino_serial = SerialConnector.get_connection()
    start_wait = True
    while video.isOpened():
        ret, frame = video.read()
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        for sensor in range(constant.SENSOR_DATA_NUMBER):
            arduino_serial.write(csv_data[value_number][sensor] + '/')
            print csv_data[value_number][sensor]
        value_number += 1
        if start_wait == True:
            time.sleep(constant.START_WAIT)
            start_wait = False
        else:
            pass
        time.sleep(0.01)
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_senbay_ver()
    # main_csv_ver()
