import constant
import serial
import socket
import json
import math


class SerialConnector:
    @classmethod
    def receive(cls, arduino_serial):
        return arduino_serial.readline()

    @classmethod
    def get_connection(cls):
        return serial.Serial(constant.DEVICE_NAME, constant.BAUD_RATE)


class UDPConnector:
    @classmethod
    def send(cls, value, dstip, dstport, mysocket):
        mysocket.sendto(value, (dstip, dstport))

    @classmethod
    def get_dstip(cls):
        return constant.IP_ADDRESS

    @classmethod
    def get_dstport(cls):
        return constant.PORT_NUMBER

    @classmethod
    def make_mysocket(cls):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class SensorDataReceiver:
    @classmethod
    def set_sender(cls, mysocket):
        return mysocket.recvfrom(cls.get_buffer_size())

    @classmethod
    def get_json_data(cls, string):
        return json.loads(string.decode(constant.STRING_CODE))

    @classmethod
    def get_port_number(cls):
        return constant.PORT_NUMBER

    @classmethod
    def get_host_name(cls):
        return constant.HOST_NAME

    @classmethod
    def get_buffer_size(cls):
        return constant.BUFFER_SIZE

    @classmethod
    def make_mysocket(cls):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @classmethod
    def bind_mysocket(cls, mysocket):
        return mysocket.bind((cls.get_host_name(), cls.get_port_number()))


class HapticDataReceiver(SensorDataReceiver):
    @classmethod
    def receive_sensor_data(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        data = cls.change_data_to_angle(cls.get_socket_data(json_data))
        return data

    @classmethod
    def get_socket_data(cls, json_data):
        return json_data[constant.SOCKET]

    @classmethod
    def change_data_to_angle(cls, data):
        value = float(data) - constant.MIN_PRESSURE
        angle = constant.MAX_ANGLE - constant.MIN_ANGLE
        pressuer = constant.MAX_PRESSURE - constant.MIN_PRESSURE
        data = value * angle / pressuer + constant.MIN_ANGLE
        if data <= constant.MIN_PRESSURE:
            return constant.MIN_ANGLE
        if data >= constant.MAX_ANGLE:
            return constant.MAX_ANGLE
        return int(data)


class BicycleDataReceiver(SensorDataReceiver):
    @classmethod
    def receive_speed_and_wind_data(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        speed = cls.change_speed_to_eight_bit(cls.get_speed_data(json_data))
        wind = cls.change_wind_to_eight_bit(cls.get_wind_data(json_data))
        return [speed, wind]

    @classmethod
    def receive_speed_data(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        speed = cls.change_speed_to_eight_bit(cls.get_speed_data(json_data))
        return speed

    @classmethod
    def receive_wind_data(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        wind = cls.change_wind_to_eight_bit(cls.get_wind_data(json_data))
        return wind

    @classmethod
    def receive_acc_data(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        acc = cls.get_acc_data(json_data)
        cls.change_acc_to_eight_bit(acc)
        return acc

    @classmethod
    def receive_acc_data_with_speed(cls, mysocket):
        string, addr = cls.set_sender(mysocket)
        json_data = cls.get_json_data(string)
        acc = cls.get_acc_data(json_data)
        speed = cls.get_speed_data(json_data)
        val = cls.change_acc_to_eight_bit_with_speed(acc, speed)
        return val

    @classmethod
    def receive_acc_actuation_value(cls, pre_acc, acc):
        difference = abs(pre_acc - acc)
        val = cls.change_acc_to_eight_bit(difference)
        return val

    @classmethod
    def get_speed_data(cls, json_data):
        return json_data[constant.SPEED]

    @classmethod
    def get_wind_data(cls, json_data):
        return json_data[constant.WIND]

    @classmethod
    def get_acc_data(cls, json_data):
        acc_x = abs(json_data[constant.ACCX])
        acc_y = abs(json_data[constant.ACCY])
        acc_z = abs(json_data[constant.ACCZ])
        acc = math.sqrt(pow(acc_x, 2) + pow(acc_y, 2) + pow(acc_z, 2));
        return acc

    @classmethod
    def change_speed_to_eight_bit(cls, data):
        data = data * (constant.MAX_EIGHT_BIT / constant.MAX_SPEED)
        if data >= constant.MAX_EIGHT_BIT:
            return constant.MAX_EIGHT_BIT
        return int(data)

    @classmethod
    def change_wind_to_eight_bit(cls, data):
        data = data * (constant.MAX_EIGHT_BIT / constant.MAX_WIND)
        if data >= constant.MAX_EIGHT_BIT:
            return constant.MAX_EIGHT_BIT
        return int(data)

    @classmethod
    def change_acc_to_eight_bit(cls, data):
        val = data * (constant.MAX_EIGHT_BIT / constant.MAX_ACC) * 2
        if val > constant.MAX_EIGHT_BIT:
            return constant.MAX_EIGHT_BIT
        return int(val)

    @classmethod
    def change_acc_to_eight_bit_with_speed(cls, acc, speed):
        _acc = cls.change_acc_to_eight_bit(acc)
        _speed = cls.change_speed_to_eight_bit(speed)
        if speed < 1:
            return _speed
        return _acc

    def read_acc_data(self):
        from data import CSVReader
        values = CSVReader().read_bicycle_acc()
        return map(float, values[0])

    def get_acc_information(self, data):
        max_difference = self.get_max_acc_difference(data)
        min_difference = self.get_min_acc_difference(data)
        average = self.get_average_acc_difference(data)
        return dict(
            max_difference=max_difference,
            min_difference=min_difference,
            average=average
        )

    def get_max_acc_difference(self, data):
        return max(data)

    def get_min_acc_difference(self, data):
        return min(data)

    def get_average_acc_difference(self, data):
        return sum(data) / len(data)
