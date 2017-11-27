import constant
import serial
import socket
import json


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
        acc = cls.change_acc_to_eight_bit(cls.get_acc_data(json_data))
        return acc

    @classmethod
    def get_speed_data(cls, json_data):
        return json_data[constant.SPEED]

    @classmethod
    def get_wind_data(cls, json_data):
        return json_data[constant.WIND]

    @classmethod
    def get_acc_data(cls, json_data):
        acc_x = json_data[constant.ACCX]
        acc_y = json_data[constant.ACCY]
        acc_z = json_data[constant.ACCZ]
        return [acc_x, acc_y, acc_z]

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
        return int(data)
