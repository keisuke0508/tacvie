import cv2
import constant
from connect import *
import data

def main():
    value_number = 0
    video = data.VideoPlayer.get_video()
    csv_data = data.CSVReader().read_csv_test()
    arduino_serial = SerialConnector.get_connection()
    while video.isOpened():
        ret, frame = video.read()
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        for sensor in range(constant.SENSOR_DATA_NUMBER):
            arduino_serial.write(csv_data[value_number][sensor] + '/')
        value_number += 1
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
