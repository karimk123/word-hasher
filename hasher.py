import hashlib
import pyperclip


# With terminal:

'''

word  = str(input("Enter a word to hash: ")).encode()

print(f"hashed value of {word.decode()}: \n{hashlib.blake2b(word).hexdigest()}")

copy = input("Do you want to copy hash to clipboard? (Y/n) ")

if(copy == "Y" or copy == "y" or copy == "yes"):
    pyperclip.copy(hashlib.blake2b(word).hexdigest())
    print("Hash copied !")
else:
    pass   
'''

# with  GUI :

from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('hasher_design.ui', self)
       
       # self.findChild(QtWidgets.QPushButton, 'HelloBtn').clicked.connect(self.hello)
        self.hashButton.clicked.connect(self.startHash)
        
        self.show()

    def startHash(self):
        self.word = str(self.lineEdit.text()).encode()
        self.label_2.setText(hashlib.blake2b(self.word).hexdigest())
        self.setGeometry(360,250,660, 300)
        self.copyButton.setEnabled(True)
        self.copyButton.clicked.connect(self.copyHash)
        

    def copyHash(self):
        pyperclip.copy(hashlib.blake2b(self.word).hexdigest())
        print("Copied!") 
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
