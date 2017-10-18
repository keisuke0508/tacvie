import csv
import random

class Test:
    def __init__(self):
        pass

    def main(self):
        data = self.makeData()
        self.writeData(data)
        print data

    def makeData(self):
        data = []
        for x in range(100):
            factor = []
            for x in range(3):
                factor.append(random.randint(0, 999))
            data.append(factor)
        return data

    def writeData(self, data):
        csv_file = open('test.csv', 'w')
        csv_writer = csv.writer(csv_file, lineterminator='\n')
        csv_writer.writerows(data)
        csv_file.close()

if __name__ == '__main__':
    Test().main()
