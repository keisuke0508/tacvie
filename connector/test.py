from connect import BicycleDataReceiver

data = BicycleDataReceiver().read_acc_data()
info = BicycleDataReceiver().get_acc_information(data)
print info
