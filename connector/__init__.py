import cv2
import time
import sys
import constant
from connect import SerialConnector, SensorDataReceiver
from connect import HapticDataReceiver, BicycleDataReceiver
import data


class SensingMain:
    def haptic(self):
        import constant
        from connect import SerialConnector, UDPConnector
        import data
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
            except Exception:
                data.CSVMaker().make_csv_test(csv_data)
                break

    def bicycle_acc(self):
        from connect import SensorDataReceiver, BicycleDataReceiver
        from data import CSVMaker
        import sys
        mysocket = SensorDataReceiver.make_mysocket()
        SensorDataReceiver.bind_mysocket(mysocket)
        data = []
        while True:
            try:
                acc = BicycleDataReceiver.receive_acc_data(mysocket)
                data.append(acc)
            except KeyboardInterrupt:
                CSVMaker().write_bicycle_acc(data)
                sys.exit()
            except Exception:
                pass


class ActuationMain:
    def haptic_senbay_ver(self):
        mysocket = SensorDataReceiver.make_mysocket()
        SensorDataReceiver.bind_mysocket(mysocket)
        arduino_serial = SerialConnector.get_connection()
        while True:
            try:
                sensor_data = HapticDataReceiver.receive_sensor_data(mysocket)
                arduino_serial.write(str(sensor_data) + '/')
                # print sensor_data
            except KeyboardInterrupt:
                arduino_serial.close()
                sys.exit()
            except Exception:
                pass

    def haptic_csv_ver(self):
        value_number = 0
        video = data.VideoPlayer.get_video()
        csv_data = data.CSVReader().read_csv()
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
            if start_wait is True:
                time.sleep(constant.START_WAIT)
                start_wait = False
            else:
                pass
            time.sleep(0.01)
        video.release()
        cv2.destroyAllWindows()

    def haptic_csv_ver_test(self):
        value_number = 0
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
            if start_wait is True:
                time.sleep(constant.START_WAIT)
                start_wait = False
            else:
                pass
            time.sleep(0.01)
        video.release()
        cv2.destroyAllWindows()

    def bicycle_senbay_speed_ver(self):
        mysocket = SensorDataReceiver.make_mysocket()
        SensorDataReceiver.bind_mysocket(mysocket)
        arduino_serial = SerialConnector.get_connection()
        while True:
            try:
                speed = BicycleDataReceiver.receive_speed_data(mysocket)
                arduino_serial.write(chr(speed))
            except KeyboardInterrupt:
                arduino_serial.close()
                sys.exit()
            except KeyError:
                print "System fail to find data."
            except Exception:
                pass

    def bicycle_senbay_acc_ver(self):
        mysocket = SensorDataReceiver.make_mysocket()
        SensorDataReceiver.bind_mysocket(mysocket)
        arduino_serial = SerialConnector.get_connection()
        pre_acc = 0
        while True:
            try:
                acc = BicycleDataReceiver.receive_acc_data(mysocket)
                val = BicycleDataReceiver.receive_acc_actuation_value(pre_acc,
                                                                      acc)
                arduino_serial.write(chr(val))
                pre_acc = acc
            except KeyboardInterrupt:
                arduino_serial.close()
                sys.exit()
            except KeyError:
                print "System fail to find data."
            except Exception:
                pass


class TacvieMain(SensingMain, ActuationMain):
    pass
