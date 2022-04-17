import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from aip import AipImageClassify
from django.shortcuts import render
from django.http import HttpResponseRedirect

class Ui_imageAI(object):
    def setupUi(self, imageAI):
        imageAI.setObjectName("imageAI")
        imageAI.resize(780, 550)  # 设置窗体大小
        imageAI.setGeometry(750, 320, 1024, 489)  # 设置窗体位置
        # 窗体美化
        imageAI.setStyleSheet("background-image:url(static/img/tt.png)")
        imageAI.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # 图片显示控件
        self.image = QtWidgets.QLabel(imageAI)
        self.image.setGeometry(QtCore.QRect(66, 140, 311, 301))#左方框
        self.image.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")

        self.widget = QtWidgets.QWidget(imageAI)
        self.widget.setGeometry(QtCore.QRect(96, 50, 221, 31))#选择识别类型
        self.widget.setObjectName("widget")
        # 选择识别类型
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")

        self.label_33 = QtWidgets.QLabel(imageAI)
        self.label_33.setGeometry(QtCore.QRect(700, 120, 300,320))
        self.label_33.setObjectName("label_33")

        # 下拉控件，用于选择识别类型
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # 横向布局容器，包含 self.label self.comboBox
        self.HBoxLayout = QtWidgets.QHBoxLayout(self.widget)
        self.HBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout.setObjectName("HBoxLayout")
        self.HBoxLayout.addWidget(self.label)
        self.HBoxLayout.addWidget(self.comboBox)

        self.widget2 = QtWidgets.QWidget(imageAI)
        self.widget2.setGeometry(QtCore.QRect(56, 80, 318, 31))#选择识别的图片
        self.widget2.setObjectName("widget2")
        # 选择要识别的图片
        self.label2 = QtWidgets.QLabel(self.widget2)
        self.label2.setObjectName("label2")
        # 图片路径显示
        self.lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit.setObjectName("lineEdit")
        # 图片路径选择Button
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        self.pushButton.setObjectName("pushButton")
        # 横向布局容器，包含 self.label2 self.lineEdit self.pushButton
        self.HBoxLayout2 = QtWidgets.QHBoxLayout(self.widget2)
        self.HBoxLayout2.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout2.setObjectName("HBoxLayout2")
        self.HBoxLayout2.addWidget(self.label2)
        self.HBoxLayout2.addWidget(self.lineEdit)
        self.HBoxLayout2.addWidget(self.pushButton)

        self.widget3 = QtWidgets.QWidget(imageAI)
        self.widget3.setGeometry(QtCore.QRect(400, 50, 281, 401))#显示识别结果
        self.widget3.setObjectName("widget3")
        # 显示识别的结果
        self.label3 = QtWidgets.QLabel(self.widget3)
        self.label3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label3.setWordWrap(True)
        self.label3.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        self.label3.setObjectName("label3")
        # 复制Button
        self.pushButton2 = QtWidgets.QPushButton(self.widget3)
        self.pushButton2.setObjectName("pushButton2")
        # 垂直布局容器，包含 self.label3 self.pushButton2
        self.VBoxLayout = QtWidgets.QVBoxLayout(self.widget3)
        self.VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.VBoxLayout.setObjectName("VBoxLayout")
        self.VBoxLayout.addWidget(self.label3)
        self.VBoxLayout.addWidget(self.pushButton2)

        self.retranslateUi(imageAI)

        QtCore.QMetaObject.connectSlotsByName(imageAI)
    def retranslateUi(self, imageAI):
        _translate = QtCore.QCoreApplication.translate

        imageAI.setWindowTitle(_translate("imageAI", "奶茶小料图像识别"))

        self.label.setText(_translate("imageAI", "选择识别类型"))
        self.label_33.setText(_translate("imageAI", "特征检测"))
        self.comboBox.setItemText(0, _translate("imageAI", "奶茶小料"))

        self.label2.setText(_translate("imageAI", "选择要识别的图片"))

        self.pushButton.setText(_translate("imageAI", "..."))
        self.pushButton.clicked.connect(self.openfile)

        self.label3.setText(_translate("imageAI", "识别结果展示"))

        self.pushButton2.setText(_translate("imageAI", "复制结果"))
        self.pushButton2.clicked.connect(self.copyText)

    def openfile(self):
        self.path = QFileDialog.getOpenFileName(self.widget2, "选择要识别的图片", "/", "Image Files(*.jpg *.png")
        print(self.path)
        if not self.path[0].strip():
            pass
        else:
            self.label_33.setPixmap(QPixmap('grey1.png'))
            self.label_33.setScaledContents(True)
            self.lineEdit.setText(self.path[0])
            pixmap = QPixmap(self.path[0])
            scaledPixmap = pixmap.scaled(QtCore.QSize(311, 301), aspectRatioMode=Qt.KeepAspectRatio)
            self.image.setPixmap(scaledPixmap)
            self.image.show()
            self.imageDetect()
            pass

    def copyText(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.label3.text())

    def imageDetect(self):
        '''
        图片识别主函数，通过检测 comboBox 中的值来进行相应的识别
        :return:
        '''
        # 通用物体识别
        if self.comboBox.currentText() == "通用物体":
            AI = AI_image_classify()
            result = AI.get_general(self.path[0])
            text = ''
            for key, value in result[0].items():
                if result[0].key == 'has_calorie':
                    break
                else:
                    text = text + str(key) + ':' + str(value)
                           # + '\n'
                    # text = text + '\n'
            self.label3.setText(text)

        # 奶茶小料识别
        elif self.comboBox.currentText() == "奶茶小料":
            AI = AI_image_classify()
            result = AI.get_dish(self.path[0])
            text = ''
            for key, value in result[0].items():
                if str(key) == 'has_calorie':
                    # del a['语文']
                    continue
                    # result['precision'] = result['probability']
                    # del result['probability']
                    # result.update({'precision': result.pop('probability')})
                    # result["precision"] = result.pop("probability")
                    # str(key) = 'precision'
                else:
                    text = text + str(key) + ':' + str(value) + '\n'
                    text = text + '\n'
            self.label3.setText(text)


class AI_image_classify(object):

    AppID = '25705158'
    API_Key = 'BL8QO2DZLD1SCHdvFfyC0ghU'
    Secret_Key = 'XauV1mzSZgNmIAY06elwUQ2d2l8GB5t2'
    client = AipImageClassify(AppID, API_Key, Secret_Key)

    def get_file_content(self, filePath):
        '''
        读取图片
        :param filePath: 图片路径
        :return:
        '''
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_general(self, filePath):
        '''
        通用物体识别
        :param filePath: 读取的图片的路径
        :return: AI识别的结果
        '''
        image = self.get_file_content(filePath)
        return self.client.advancedGeneral(image)['result']

    def get_dish(self, filePath):
        '''
        菜品识别
        :param filePath: 读取的图片的路径
        :return: AI识别的结果
        '''
        image = self.get_file_content(filePath)
        return self.client.dishDetect(image)['result']



a=QtWidgets.QApplication(sys.argv)
app =a
MainWindow = QtWidgets.QMainWindow()
Ui = Ui_imageAI()
Ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
