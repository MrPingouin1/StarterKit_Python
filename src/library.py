class Library:
    def __init__(self, id, signUpSpeed, scanningSpeed):
        self.id = id
        self.signUpSpeed = int(signUpSpeed)
        self.scanningSpeed = int(scanningSpeed)
        self.listBooks = []
        self.bookScanned = []
        self.total_score = int(0)
        self.temp_max= int(0)
    
    def addBook(self, book):
        self.listBooks.append(book)
