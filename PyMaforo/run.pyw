import sys, serial, time, os
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,QFrame,
    QVBoxLayout, QDialog,QLabel,QProgressBar,QMessageBox)
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap

serial_port = 'COM4'
baudrate = 115200

def _ConnectToArduino():     
    arduino = serial.Serial(serial_port, baudrate, timeout=.1)
    time.sleep(2) #give the connection two seconds to settle
    return arduino

def _sendData(arduino,option):
    try:
        with arduino:
            arduino.write(option.encode()) #read the data from the arduino
    except:
        print("Failed to connect on")

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Pymaforo v1.1")
        self.setFixedSize(250, 400)
        # Create widgets
        title = QLabel()
        lbl = QLabel()
        img = QLabel(self)
        
        pixmap = QPixmap('semaforo.jpg')
        img.setPixmap(pixmap)
        img.resize(80,100)
        
        title.setText("Sistema Pymaforo")
        lbl.setText("Ingrese el ID del semaforo:")
        
        title.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        title.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        lbl.setAlignment(Qt.AlignBottom| Qt.AlignLeft)
        
        self.edit = QLineEdit("201")
        self.button1 = QPushButton('Solicitar paso')
        self.button2 = QPushButton("Solicitar paso con prioridad")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(img)
        layout.addWidget(lbl)
        layout.addWidget(self.edit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button1.clicked.connect(self.giveway)
        self.button2.clicked.connect(self.givewaypriori)

    # Greets the user
    def giveway(self):
        if self.edit.text() == "201":
            print ("Se ha solicitado el paso al semáforo #" +self.edit.text()+" correctamente")
    
            _sendData(_ConnectToArduino(),'A')
            QMessageBox.about(self, "Aviso", "Se ha solicitado el paso al semáforo #" +self.edit.text()+" correctamente")
    def givewaypriori(self):
        if self.edit.text() == "201":
            print ("Se ha solicitado el paso con prioridad al semáforo #" +self.edit.text()+" correctamente")
    
            _sendData(_ConnectToArduino(),'B')
            QMessageBox.about(self, "Aviso", "Se ha solicitado el paso al semáforo #" +self.edit.text()+" correctamente")
    

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
