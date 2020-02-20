from book import Book
from library import Library
import csv


class FileParser:
    def __init__(self, fileDir, separator, isHeader):
        self.file = fileDir
        self.separator = separator
        self.isHeader = isHeader

    def getData(self):
        # pk r 
        result = []
        with open(self.file, 'r') as file:
            reader = csv.reader(file, delimiter=self.separator)
            for row in reader:
                tempo = Data(row[0], row[1], row[2])
                result.append(tempo)
                
        return result

