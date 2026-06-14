# static vs non static

class WordSetNonStatic:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(self, text):
        return text.replace('!', '').replace('.', '').replace(',', '').replace('/', '').lower()
    
    def printText(self):
        print(self.words)
    
wordSet = WordSetNonStatic()
wordSet.addText('This is a very interting speech. He is a GOAT!')
wordSet.printText()




