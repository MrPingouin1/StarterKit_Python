class Data:
    def __init__(self, cuisiniere, fourchette, menteau):
        self.cuisiniere = cuisiniere
        self.fourchette = fourchette
        self.menteau = menteau
    
    def print(self):
        print(self.cuisiniere + ' : ' + self.fourchette + ' : ' + self.menteau)