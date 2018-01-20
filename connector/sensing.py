from debug import Timer

def haptic():
    import constant
    from connect import SerialConnector, UDPConnector
    import data
    import sys
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
        except KeyboardInterrupt:
            data.CSVMaker().make_csv_test(csv_data)
            sys.exit()
        except Exception:
            print "fail to get data"


def bicycle_acc():
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


def manage(act):
    if act == 'h' or act == 'haptic':
        haptic()
        # haptic_csv_ver()
    elif act == 'b' or act == 'bicycle':
        bicycle_acc()
    else:
        main()


def main():
    print "input 'h' or 'b' (haptic or bicycle)."
    act = raw_input()
    manage(act)


if __name__ == "__main__":
    main()
