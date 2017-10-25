import csv
import os
import cv2
import constant

class CSVMaker:
    def make_csv(self, values):
        path = self.get_csv_path()
        self.change_dir_to_csv(path)
        filename = self.get_filename()
        self.change_values_to_number(values)
        self.write_csv(filename, values)

    def make_csv_test(self, values):
        filename = constant.CSV_TEST_FILE
        self.change_values_to_number(values)
        self.write_csv(filename, values)

    def get_csv_path(self):
        return constant.CSV_PATH

    def change_dir_to_csv(self, path):
        os.chdir(path)

    def get_filename(self):
        num = 1
        filename = ''
        while True:
            filename = 'data' + str(num) + '.csv'
            if os.path.exists(filename) == True:
                num = num + 1
            else:
                break
        return filename

    def change_values_to_number(self, values):
        try:
            for sensor_data in range(len(values)):
                values[sensor_data] = map(int, values[sensor_data])
        except:
            for sensor_data in range(len(values)):
                values[sensor_data] = map(float, values[sensor_data])

    def write_csv(self, filename, values):
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerows(values)


class CSVReader:
    def read_csv(self):
        path = self.get_csv_path()
        self.change_dir_to_csv(path)
        filename = constant.CSV_FILE
        csv_data = self.get_data_from_csv(filename)
        self.change_number_to_string(csv_data)
        return csv_data

    def read_csv_test(self):
        filename = constant.CSV_FILE
        csv_data = self.get_data_from_csv(filename)
        self.change_number_to_string(csv_data)
        return csv_data

    def get_csv_path(self):
        return constant.CSV_PATH

    def change_dir_to_csv(self, path):
        os.chdir(path)

    def get_data_from_csv(self, filename):
        data = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, lineterminator='\n')
            for row in csv_reader:
                data.append(row)
            return data

    def change_number_to_string(self, csv_data):
        for sensor_data in range(len(csv_data)):
            csv_data[sensor_data] = map(str, csv_data[sensor_data])


class VideoPlayer:
    def play_video_test(self):
        video = self.get_video()
        while video.isOpened():
            ret, frame = video.read()
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

    @classmethod
    def get_video(self):
        filename = constant.VIDEO_PATH + constant.VIDEO_FILE
        return cv2.VideoCapture(filename)
