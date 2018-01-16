import time

class Timer:
    @classmethod
    def get_unix_time(cls):
        return time.time()

    @classmethod
    def get_elapsed_time(cls, time1, time2):
        """
        calculating elapsed time from two unix time
        :param time1: earlier unix time(float)
        :param time2: later unix time(float)
        :return: time2 - time1
        :rtype: float
        """
        return time2 - time1