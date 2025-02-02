class Mystring:
    def getstring(self):
        self.sent=input("Enter sentence: ")
    def printstring(self):
        print("Upper case sentence:", self.sent.upper())

string = Mystring()
string.getstring()
string.printstring()