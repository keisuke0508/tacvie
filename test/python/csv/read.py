import csv

class Test:
    def __init__(self):
        pass

    def main(self):
        filename = 'test.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f, lineterminator='\n')
            for row in reader:
                print row

if __name__ == '__main__':
    Test().main()
