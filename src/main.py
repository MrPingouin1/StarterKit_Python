from book import Book
from library import Library
import csv

dataFile = 'ressources/b_read_on.txt'
output = 'target/out.txt'

booksList = []
libraryList = []
maxDays = 0

# read ---------------------------------------------------------------------------------
with open(dataFile, 'r') as file:
    tempoReader = csv.reader(file, delimiter=' ')
    reader = list(tempoReader)

    nbBooksTotal = int(reader[0][0])
    nbLibrary = int(reader[0][1])
    maxDays = int(reader[0][2])

    i = 0
    for row in reader[1]:
        i = i +1
        booksList.append(Book(i,row))
    
    idLib=0
    for j in range(2, len(reader)-1, 2):
        print(reader[j])    
        tempoLibrary = Library(idLib, reader[j][1], reader[j][2])
        idLib += 1
        nbBooksLib = int(reader[j][0])
        for k in range(nbBooksLib-1):
            tempoLibrary.addBook(booksList[int(reader[j+1][k])])
        libraryList.append(tempoLibrary)

# print (libraryList[-1].listBooks[-1].id)

# scan ------------------------------------------------------------------------------------
listLibraryScan = []

# write -----------------------------------------------------------------------------------
with open(dataFile, 'w') as file:
    file.write(len(listLibraryScan) + '\n\r')

    for library in listLibraryScan:
        file.write(library.id + ' ' + len(library.bookScanned) + '\n\r')
        for book in library.bookScanned:
            file.write(book.id + ' ')
        
        file.write('\n\r')

# end -------------------------------------------------------------------------------------
print('ended')