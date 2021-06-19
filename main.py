from PyQt5 import QtWidgets, uic, QtGui
import sys,random
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.title="sefa"
        self.table=self.tableWidget
        #print(self.table)
        self.hesapla.clicked.connect(self.calculate)
        # self.table.setItem(1, 1, QTableWidgetItem("text1"))
        self.show()

    def measurements(self):
        # M1 değerleri
        self.m1= self.table.item(0, 0).text()
        self.m2 = self.table.item(1, 0).text()
        self.m3 = self.table.item(2, 0).text()
        self.m4 = self.table.item(3, 0).text()
        self.m5 = self.table.item(4, 0).text()
        self.m6 = self.table.item(5, 0).text()
        self.m7 = self.table.item(6, 0).text()
        self.m8 = self.table.item(7, 0).text()

        # M/E output değerleri
        self.out1= self.table.item(0, 1).text()
        self.out2 = self.table.item(1, 1).text()
        self.out3 = self.table.item(2, 1).text()
        self.out4 = self.table.item(3, 1).text()
        self.out5 = self.table.item(4, 1).text()
        self.out6 = self.table.item(5, 1).text()
        self.out7 = self.table.item(6, 1).text()
        self.out8 = self.table.item(7, 1).text()
        # sfc  değerleri
        self.sfc1 = self.table.item(0, 2).text()
        self.sfc2 = self.table.item(1, 2).text()
        self.sfc3 = self.table.item(2, 2).text()
        self.sfc4 = self.table.item(3, 2).text()
        self.sfc5 = self.table.item(4, 2).text()
        self.sfc6 = self.table.item(5, 2).text()
        self.sfc7 = self.table.item(6, 2).text()
        self.sfc8 = self.table.item(7, 2).text()
        # Cf değerleri
        self.cf1 = self.table.item(0, 3).text()
        self.cf2 = self.table.item(1, 3).text()
        self.cf3 = self.table.item(2, 3).text()
        self.cf4 = self.table.item(3, 3).text()
        self.cf5 = self.table.item(4, 3).text()
        self.cf6 = self.table.item(5, 3).text()
        self.cf7 = self.table.item(6, 3).text()
        self.cf8 = self.table.item(7, 3).text()
        # dwt değerleri
        self.dwt1 = self.table.item(0, 4).text()
        self.dwt2 = self.table.item(1, 4).text()
        self.dwt3 = self.table.item(2, 4).text()
        self.dwt4 = self.table.item(3, 4).text()
        self.dwt5 = self.table.item(4, 4).text()
        self.dwt6 = self.table.item(5, 4).text()
        self.dwt7 = self.table.item(6, 4).text()
        self.dwt8 = self.table.item(7, 4).text()
        # speed değerleri
        self.speed1 = self.table.item(0, 5).text()
        self.speed2 = self.table.item(1, 5).text()
        self.speed3 = self.table.item(2, 5).text()
        self.speed4 = self.table.item(3, 5).text()
        self.speed5 = self.table.item(4, 5).text()
        self.speed6 = self.table.item(5, 5).text()
        self.speed7 = self.table.item(6, 5).text()
        self.speed8 = self.table.item(7, 5).text()

    def requiredIEXX(self):
        combomuz = str(self.comboBox.currentText()) #Gemi tipin
        dwt = float(self.dwt.text()) # Dwt değerin
        if combomuz =="Container Ship":
            self.first = 174.22*(0.7*dwt)**(-0.201)
            print(self.first)
        elif combomuz == "Oil Tanker":
            self.first = 1217.8 * (dwt ** (-0.488))

        # Required IEXX
        elif combomuz == "Bulk Carrier":
            self.first = 961.79*(dwt**(-0.477))
            print(self.first)
        else:
            print("Hata oluştu 23. satır")

    def calculate(self):
        self.measurements()
        self.requiredIEXX()
        liste = [[self.m1,self.out1,self.sfc1,self.cf1,self.dwt1,self.speed1],
                 [self.m2,self.out2,self.sfc2,self.cf2,self.dwt2,self.speed2],
                 [self.m3,self.out3,self.sfc3,self.cf3,self.dwt3,self.speed3],
                 [self.m4,self.out4,self.sfc4,self.cf4,self.dwt4,self.speed4],
                 [self.m5,self.out5,self.sfc5,self.cf5,self.dwt5,self.speed5],
                 [self.m6,self.out6,self.sfc6,self.cf6,self.dwt6,self.speed6],
                 [self.m7,self.out7,self.sfc7,self.cf7,self.dwt7,self.speed7],
                 [self.m8,self.out8,self.sfc8,self.cf8,self.dwt8,self.speed8]]
        #print(self.out2)
        self.attained_values = []
        self.m_list = []
        for i in liste:
            # print(float(i[1])+float(i[2]))
            self.sonuc = float(i[1]) * float(i[2]) * float(i[3]) / (float(i[4]) * float(i[5]))
            self.attained_values.append(self.sonuc)
            self.m_list.append(i[0])
        #print(self.attained_values)
        # self.attainedIEXX()
        # print(self.SFC*self.ME*self.CF/self.Capacity*self.Vref)
        self.update_graph()

    def update_graph(self):
        # print(self.attained_values)
        names = self.m_list
        # attained_values = list([self.deger1,self.deger5,self.deger1,self.deger5,self.deger1,self.deger5,self.deger1,self.deger5])
        required_values = list([self.first,self.first,self.first,self.first,self.first,self.first,self.first,self.first])
        self.MplWidget.canvas.axes.clear()
        top_value = max(max(self.attained_values), max(required_values))
        self.MplWidget.canvas.axes.set_ylim(0, top_value+1)
        self.MplWidget.canvas.axes.plot(names, self.attained_values)
        self.MplWidget.canvas.axes.plot(names,required_values)
        self.MplWidget.canvas.axes.legend(('attained', 'required'), loc='lower right')
        self.MplWidget.canvas.axes.set_title('Attained EEXI - Required EEXI')
        #self.MplWidget.canvas.axes.plot([0], [3.14], 'o')
        self.MplWidget.canvas.axes.text(0, self.attained_values[0], round(self.attained_values[0],2))
        self.MplWidget.canvas.axes.text(1, self.attained_values[1], round(self.attained_values[1],2))
        self.MplWidget.canvas.axes.text(2, self.attained_values[2], round(self.attained_values[2],2))
        self.MplWidget.canvas.axes.text(3, self.attained_values[3], round(self.attained_values[3],2))
        self.MplWidget.canvas.axes.text(4, self.attained_values[4], round(self.attained_values[4],2))
        self.MplWidget.canvas.axes.text(5, self.attained_values[5], round(self.attained_values[5],2))
        self.MplWidget.canvas.axes.text(6, self.attained_values[6], round(self.attained_values[6],2))
        self.MplWidget.canvas.axes.text(7, self.attained_values[7], round(self.attained_values[7],2))
        self.MplWidget.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()

    app.exec_()
