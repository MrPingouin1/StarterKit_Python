class Library:
    def __init__(self, id, signUpSpeed, scanningSeed):
        self.id = id
        self.signUpSpeed = signUpSpeed
        self.scanningSeed = scanningSeed
        self.listBooks = []
        self.bookScanned = []
    
    def addBook(self, book):
        self.listBooks.append(book)
