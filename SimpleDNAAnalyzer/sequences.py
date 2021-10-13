import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from Bio.Seq import Seq

class Sequences(QDialog):
    
    def __init__(self):
        super().__init__()
        loadUi("seq.ui", self)
        self.show()
        self.okButton.clicked.connect(self.analyze)
        self.resetButton.clicked.connect(self.reset)
        self.DNAline.textEdited.connect(self.calculate_length)
    
    def analyze(self, reset = False):
        self.seq = Seq(self.DNAline.text())

        self.cDNAline.setText(str(self.seq.complement()))

        self.revcDNAline.setText(str(self.seq.reverse_complement()))

        self.RNAline.setText(str(self.seq.transcribe()))

        self.no_codon = len(self.seq) % 3
        if  self.no_codon == 0:
            self.aminoline.setText(str(self.seq.translate()))
        else:
            self.aminoline.setText(str(self.seq[:-self.no_codon].translate()))

        self.aminolengthval.setText(
            str(len(self.seq[:-self.no_codon].translate(to_stop=True))))

    def calculate_length(self):
        self.DNAlengthval.setText(str(len(self.DNAline.text())))

    def reset(self):
        self.DNAline.setText(str(''))
        self.cDNAline.setText(str(''))
        self.revcDNAline.setText(str(''))
        self.RNAline.setText(str(''))
        self.aminoline.setText(str(''))
        self.aminolengthval.setText(str('0'))
        self.DNAlengthval.setText(str('0'))   
      

if __name__ == "__main__":
    aplikacja = QApplication(sys.argv)
    okno = Sequences()
    okno.show()
    sys.exit(aplikacja.exec_())

