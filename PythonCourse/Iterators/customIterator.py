__author__ = "ResearchInMotion"

class Alphabet:
    def __init__(self):
        self.letter = "SAHILNAGPAL"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letter) - 1:
            raise StopIteration
        self.index +=1
        return self.letter[self.index]

alphabet = Alphabet()
for vals in alphabet:
    print(vals)