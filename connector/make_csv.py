import csv
import os
import data

class CSVMaker:
    def make_csv(self, values):
        address = self.get_csv_address()
        self.change_dir_to_csv(address)
        filename = self.get_filename()
        self.write_csv(filename, values)

    def make_csv_test(self, values):
        filename = 'test.csv'
        self.write_csv(filename, values)

    def get_csv_address(self):
        return data.CSV_ADDRESS

    def change_dir_to_csv(self, address):
        os.chdir(address)

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

    def write_csv(self, filename, values):
        with open(filename, 'w') as csv_file:
            csv_file = open(filename, 'w')
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerows(values)
