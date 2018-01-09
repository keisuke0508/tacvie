from connector.connect import SerialConnector
from connector.connect import HapticDataReceiver, BicycleDataReceiver


class AppHapticProcesser:
    def __init__(self):
        self.mysocket = HapticDataReceiver.make_mysocket()
        HapticDataReceiver.bind_mysocket(self.mysocket)
        self.arduino_serial = SerialConnector.get_connection()

    def process(self):
        try:
            sensor_data = HapticDataReceiver.receive_sensor_data(self.mysocket)
            self.arduino_serial.write(str(sensor_data) + '/')
        except Exception:
            pass

    def close(self):
        self.arduino_serial.close()


class AppBicycleProcesser:
    def __init__(self):
        self.mysocket = BicycleDataReceiver.make_mysocket()
        BicycleDataReceiver.bind_mysocket(self.mysocket)
        self.arduino_serial = SerialConnector.get_connection()

    def process(self):
        try:
            speed = BicycleDataReceiver.receive_speed_data(self.mysocket)
            self.arduino_serial.write(chr(speed))
        except Exception:
            pass

    def close(self):
        self.arduino_serial.close()
