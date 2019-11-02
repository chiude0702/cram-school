import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

class WinForm(QMainWindow):
    def __init__ (self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setGeometry(400,150,1138,799)  #視窗起始位置大小
        layout = QVBoxLayout()
        self.btn1 = QPushButton('開啟圖片',self)
        self.btn1.setGeometry(10,10,60,30) #按鈕位置大小
        self.btn1.clicked.connect(self.open)

        self.btn2 = QPushButton('關閉視窗',self)
        self.btn2.setGeometry(970,10,60,30) #按鈕位置大小
        self.btn2.clicked.connect(self.close)

        self.btn3 = QPushButton('存檔',self)
        self.btn3.setGeometry(900,10,60,30) #按鈕位置大小
        self.btn3.clicked.connect(self.save)

        self.btn4 = QPushButton('HSV',self)
        self.btn4.setGeometry(80,10,60,30) #按鈕位置大小
        self.btn4.clicked.connect(self.HSV)

        self.btn5 = QPushButton('模糊',self)
        self.btn5.setGeometry(150,10,60,30) #按鈕位置大小
        self.btn5.clicked.connect(self.blurre)

        self.btn6 = QPushButton('灰階',self)
        self.btn6.setGeometry(220,10,60,30) #按鈕位置大小
        self.btn6.clicked.connect(self.gray)

        self.btn7 = QPushButton('二值化',self)
        self.btn7.setGeometry(290,10,60,30) #按鈕位置大小
        self.btn7.clicked.connect(self.canny)

        self.btn8 = QPushButton('膨脹',self)
        self.btn8.setGeometry(360,10,60,30) #按鈕位置大小
        self.btn8.clicked.connect(self.dilated)

        self.btn9 = QPushButton('侵蝕',self)
        self.btn9.setGeometry(430,10,60,30) #按鈕位置大小
        self.btn9.clicked.connect(self.eroded)

        self.btn10 = QPushButton('高倍偵測',self)
        self.btn10.setGeometry(500,10,60,30) #按鈕位置大小
        self.btn10.clicked.connect(self.circle)

        self.btn11 = QPushButton('低倍偵測',self)
        self.btn11.setGeometry(570,10,60,30) #按鈕位置大小
        self.btn11.clicked.connect(self.circle1)

        self.label = QLabel('',self)
        self.label.setGeometry(10,45,554,739)
        layout.addWidget(self.label)
        self.label2 = QLabel('',self)
        self.label2.setGeometry(574,45,554,739)
        layout.addWidget(self.label2)
        self.setLayout(layout)
        self.setWindowTitle('opencv圖像處理')
    def open(self):
        File,_ = QFileDialog.getOpenFileName(self,'Open File','C:\\','Images Files (*.jpg *.jpeg *.png)')  # all Files(*)
        if File is '':
            return
        self.img = cv2.imread(File,-1)
        if self.img.size ==1:
            return
        self.Show()
        self.refreshShow()
    def close(self):
        pass
    def save(self):
        pass
    def HSV(self):
        pass
    def blurre(self):
        if self.img.size ==1:
            return
        self.img = cv2.GaussianBlur(self.img,(9,9),0)
        self.refreshShow()
    def gray(self):
        pass
    def canny(self):
        pass
    def dilated(self):
        pass
    def eroded(self):
        pass
    def circle(self):
        pass
    def circle1(self):
        pass
    def Show(self):  
       
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        
        self.label.setPixmap (QPixmap(self.qImg))
        self.label.setScaledContents (True)
        
    def refreshShow(self):
        
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
       
        self.label2.setPixmap (QPixmap(self.qImg))
        self.label2.setScaledContents (True)
        
    def GRAYrefreshShow(self):
        height, width = self.img.shape
        self.qImg = QImage(self.img.data, width, height,width, 
                            QImage.Format_Grayscale8)
        self.label2.setPixmap(QPixmap.fromImage(self.qImg))
        self.label2.setScaledContents (True)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())