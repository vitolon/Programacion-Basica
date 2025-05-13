import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QGridLayout)

app = QApplication(sys.argv)

class Calculadora(QWidget):
    def __init__(self):   
         QWidget.__init__(self)
         self.setWindowTitle("TRALALERO TRALALA")
         self.A = QLineEdit("0")
         self.B = QLineEdit("0")
         self.sumar =QPushButton("+")
         self.restar = QPushButton("-")
         self.multimplicar = QPushButton("*")
         self.dividir = QPushButton("/")
         self.resultado = QLabel("Resultado")
         
         grid = QGridLayout(self)
         grid.addWidget(self.A,0,1,1,3)
         grid.addWidget(self.B,1,1,1,3)
         grid.addWidget(self.sumar,2,0)
         grid.addWidget(self.restar,2,1)
         grid.addWidget(self.multimplicar,2,2)
         grid.addWidget(self.dividir,2,3)
         grid.addWidget(self.resultado,3,1)
         grid.addWidget(QLabel("A"),0,0)
         grid.addWidget(QLabel("B"),1,0)
         grid.addWidget(QLabel("RPTA"),3,0)
         
         self.sumar.clicked.connect(self.suma)
         self.restar.clicked.connect(self.resta)
         self.multimplicar.clicked.connect(self.multiplicacion)
         self.dividir.clicked.connect(self.division)
         self.show()

    
def suma(self):
    
        r = float(self.A.text()) + float(self.B.text())
        self.resultado.setText(str(r))
def resta (self):
      r = float(self.A.Text()) - float(self.B.text())
      self.resultado.setText(str(r))
def multiplicacion (self):
      r=float(self.A.text()) * float(self.B.text())
      self.resultado.setText(str(r))
def division (self):
    r = float (self.A.text()) / float (self.B.text())
    self.resultado.setText(str(r))

      

calc = Calculadora()

sys.exit(app.exec_())



