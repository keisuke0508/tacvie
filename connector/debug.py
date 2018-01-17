import time

class Timer:
    @classmethod
    def get_unix_time(cls):
        return time.time()

    @classmethod
    def get_elapsed_time(cls, time1, time2, printer=True):
        """
        calculating elapsed time from two unix time
        :param time1: earlier unix time(float)
        :param time2: later unix time(float)
        :return: time2 - time1
        :rtype: float
        """
        time = time2 - time1
        if printer:
            print time
        return time

    @classmethod
    def calculate_time_data(cls, time_list):
        max_val = max(time_list)
        min_val = min(time_list)
        length = len(time_list)
        sum_val = sum(time_list)
        average = sum_val / length
        data = dict(
            max_val=max_val,
            min_val=min_val,
            length=length,
            sum_val=sum_val,
            average=average
        )
        print data


class SensorDataPrinter:
    @classmethod
    def calculate_acc_data(cls, values):
        max_val = max(values)
        min_val = min(values)
        length = len(values)
        sum_val = sum(values)
        average = sum_val / length
        data = dict(
            max_val=max_val,
            min_val=min_val,
            length=length,
            sum_val=sum_val,
            average=average
        )
        print data