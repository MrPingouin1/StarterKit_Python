from book import Book
from library import Library

import csv

class Model:
    def __init__(self):
        self.booksList = []
        self.libraryList = []
        self.maxDays = 0
        self.listLibraryScan = []

    def loadData(self, dataFile):
        with open(dataFile, 'r') as file:            
            reader = list(csv.reader(file, delimiter=' '))

            nbBooksTotal = int(reader[0][0])
            nbLibrary = int(reader[0][1])
            self.maxDays = int(reader[0][2])

            i = 0
            for row in reader[1]:
                self.booksList.append(Book(i,row))
                i = i +1
            
            idLib=0
            for j in range(2, len(reader)-1, 2):   
                tempoLibrary = Library(idLib, reader[j][1], reader[j][2])
                idLib += 1
                nbBooksLib = int(reader[j][0])
                for k in range(nbBooksLib):
                    tempoLibrary.addBook(self.booksList[int(reader[j+1][k])])
                self.libraryList.append(tempoLibrary)
    
    def outSolution(self, dataFile):
        with open(dataFile, 'w') as file:
            file.write(str(len(self.listLibraryScan)) + '\n')
            for library in self.listLibraryScan:
                file.write(str(library.id) + ' ' + str(len(library.bookScanned)) + '\n')
                for book in library.bookScanned:
                    file.write(str(book.id) + ' ')                
                file.write('\n')

    def stupidChoice(self):
        self.listLibraryScan=self.libraryList
        for library in self.listLibraryScan:
            library.bookScanned = library.listBooks

    def printModel(self):
        for library in self.libraryList:
            for book in library.listBooks:
                print(str(book.id))
            print('other')

    def goodOne(self):
        table = []
        for x in self.libraryList:
            score =0
            cumul_tot= 0
            cumul_jour=0
            for y in x.listBooks:
                score += y.score
            if ((len(x.listBooks)/x.scanningSpeed)>self.maxDays):
                cumul_jour=self.maxDays
                x.temp_max=self.maxDays
            else:
                cumul_jour=len(x.listBooks)/x.scanningSpeed
            x.total_score = (score/cumul_jour)
            table.append(x.total_score)

        for x in self.libraryList:
            max_x=max(table)
            value=table.index(max_x)
            self.listLibraryScan.append(self.libraryList[value])
            table.remove(max_x)
            
        for t in self.libraryList:
            for y in x.listBooks:
                for w in range(((x.temp_max-t.signUpSpeed)*t.scanningSpeed)-1):
                    x.bookScanned.append(x.listBooks[w])