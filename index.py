# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from HaarDetection import Detection
from Result import DrawTable
import cv2
#PIL强大的图形处理库
from PIL import Image
import win32ui


#haar分类器的路径
HAAR_PATH='Y:\FaceDetection\data\haarcascades'
POSITIVE_FACE='\haarcascade_frontalface_default.xml'
EYE_WITHOUTGLASS='\haarcascade_eye.xml'
EYE_WITHGLASS='\haarcascade_eye_tree_eyeglasses.xml'
LEFT_EYE='\haarcascade_lefteye_2splits.xml'
RIGHT_EYE='\haarcascade_righteye_2splits.xml'

LBP_PATH='Y:\FaceDetection\data\lbpcascades\lbpcascade_frontalface.xml'

#LBP分类器路径
LBP_FRONTFACE='lbpcascade_frontalface.xml'
LBP_PROFILEFACE='lbpcascade_profilefacexml'

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        #图像文件的路径
        self.filePath = ''
        self.detectTime=[]
        self.detectName=[]
        self.groupList={}

        Dialog.setObjectName("Dialog")
        Dialog.resize(1340, 700)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setGeometry(QRect(20, 20, 170, 600))
        self.groupBox.setObjectName("")
        self.Btn_openFile = QPushButton(self.groupBox)
        self.Btn_openFile.setGeometry(QRect(40, 40, 80, 23))
        self.Btn_openFile.setObjectName("Btn_openFile")
        self.Btn_faceDetect = QPushButton(self.groupBox)
        self.Btn_faceDetect.setGeometry(QRect(40, 90, 80, 23))
        self.Btn_faceDetect.setObjectName("Btn_faceDetect")
        self.Btn_eyeDetect = QPushButton(self.groupBox)
        self.Btn_eyeDetect.setGeometry(QRect(40, 140, 80, 23))
        self.Btn_eyeDetect.setObjectName("Btn_eyeDetect")
        self.Btn_multiDetect = QPushButton(self.groupBox)
        self.Btn_multiDetect.setGeometry(QRect(40, 190, 80, 23))
        self.Btn_multiDetect.setObjectName("Btn_multiDetect")
        self.Btn_LBPDetect = QPushButton(self.groupBox)
        self.Btn_LBPDetect.setGeometry(QRect(40, 240, 80, 23))
        self.Btn_LBPDetect.setObjectName("Btn_LBPDetect")
        self.Btn_Analysis=QPushButton(self.groupBox)
        self.Btn_Analysis.setGeometry(QRect(40,290,80,23))
        self.Btn_Analysis.setObjectName('Btn_Analysis')
        self.scaleFactor = QLabel(self.groupBox)
        self.scaleFactor.setGeometry(QRect(10, 330, 90, 20))
        self.scaleFactor.setObjectName("label_5")
        self.minNeighbors = QLabel(self.groupBox)
        self.minNeighbors.setGeometry(QRect(10, 380, 90, 20))
        self.minNeighbors.setObjectName("label_6")
        self.LE_scaleFactor = QLineEdit(self.groupBox)
        self.LE_scaleFactor.setGeometry(QRect(90, 330, 51, 21))
        self.LE_scaleFactor.setObjectName("LE_scaleFactor")
        #设置scalefactor的输入类型及输入范围
        self.LE_scaleFactor.setValidator(QDoubleValidator(1.1,2.0,1,self.LE_scaleFactor))
        self.LE_minNeighbors = QLineEdit(self.groupBox)
        self.LE_minNeighbors.setGeometry(QRect(90, 380, 51, 20))
        self.LE_minNeighbors.setObjectName("LE_minNeighbors")
        #设置minNeighbors的输入类型及输入范围
        self.LE_minNeighbors.setValidator(QIntValidator(3,6,self.LE_minNeighbors))
        self.L_scaleFactor = QLabel(self.groupBox)
        self.L_scaleFactor.setGeometry(QRect(20, 350, 120, 20))
        self.L_scaleFactor.setObjectName("L_scaleFactor")
        self.L_minNeighbors = QLabel(self.groupBox)
        self.L_minNeighbors.setGeometry(QRect(20, 400, 120, 20))
        self.L_minNeighbors.setObjectName("L_minNeighbors")


        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QRect(210, 20, 770, 600))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout=QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_1=QGraphicsView(self.groupBox_2)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.gridLayout.addWidget(self.graphicsView_1,0,0,1,1)
        self.graphicsView_2=QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QGraphicsView(self.groupBox_2)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 2, 0, 1, 1)
        self.graphicsView_4 = QGraphicsView(self.groupBox_2)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 2, 1, 1, 1)


        self.groupBox_3=QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QRect(1000,20,320,600))
        self.groupBox_3.setObjectName("groupBox_3")

        self.time_label1 = QLabel(self.groupBox_3)
        self.time_label1.setGeometry(QRect(20, 20, 100, 20))
        self.time_label1.setObjectName("time_label1")
        self.time_haarface=QLabel(self.groupBox_3)
        self.time_haarface.setGeometry(QRect(140,20,100,20))
        self.time_haarface.setObjectName("time_haarface")

        self.time_label2 = QLabel(self.groupBox_3)
        self.time_label2.setGeometry(QRect(20, 70, 100, 20))
        self.time_label2.setObjectName("time_label2")
        self.time_haareye = QLabel(self.groupBox_3)
        self.time_haareye.setGeometry(QRect(140,70,100,20))
        self.time_haareye.setObjectName("time_haareye")

        self.time_label3 = QLabel(self.groupBox_3)
        self.time_label3.setGeometry(QRect(20, 120, 100, 20))
        self.time_label3.setObjectName("time_lable3")
        self.time_haarmulti= QLabel(self.groupBox_3)
        self.time_haarmulti.setGeometry(QRect(140,120,100,20))
        self.time_haarmulti.setObjectName("time_haarmulti")

        self.time_label4 = QLabel(self.groupBox_3)
        self.time_label4.setGeometry(QRect(20, 170, 100, 20))
        self.time_label4.setObjectName("time_label4")
        self.time_LBPface = QLabel(self.groupBox_3)
        self.time_LBPface.setGeometry(QRect(140,170,100,20))
        self.time_LBPface.setObjectName("time_LBPface")


        self.retranslateUi(Dialog)
        #GUI与事件的绑定

        self.Btn_openFile.clicked.connect(self.openfileDialog)
        self.Btn_faceDetect.clicked.connect(self.MessageBox)
        self.Btn_eyeDetect.clicked.connect(self.MessageBox)
        self.Btn_multiDetect.clicked.connect(self.MessageBox)
        self.Btn_LBPDetect.clicked.connect(self.MessageBox)
        self.Btn_Analysis.clicked.connect(self.DrawResult)
        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "基于OpenCV的人脸检测系统"))
        self.groupBox.setTitle(_translate("Dialog", "操作菜单"))
        self.Btn_openFile.setText(_translate("Dialog", "打开文件"))
        self.Btn_faceDetect.setText(_translate("Dialog", "Haar人脸检测"))
        self.Btn_eyeDetect.setText(_translate("Dialog", "Haar眼睛检测"))
        self.Btn_multiDetect.setText(_translate("Dialog", "Haar混合检测"))
        self.Btn_LBPDetect.setText(_translate("Dialog", "LBP人脸检测"))
        self.Btn_Analysis.setText(_translate("Dialog",'结果分析'))
        self.scaleFactor.setText(_translate("Dialog", "scaleFactor："))
        self.minNeighbors.setText(_translate("Dialog", "minNeighbors："))
        self.L_scaleFactor.setText(_translate("Dialog", "默认值1.1（1.1-2）"))
        self.L_minNeighbors.setText(_translate("Dialog", "默认值3（3-6）"))
        self.groupBox_2.setTitle(_translate("Dialog", "人脸识别"))
        self.groupBox_3.setTitle(_translate("Dialog","结果分析"))
        self.graphicsView_1.setWindowTitle(_translate("Dialog","haar人脸检测"))
        self.graphicsView_2.setWindowTitle(_translate("Dialog", "haar眼睛检测"))
        self.graphicsView_3.setWindowTitle(_translate("Dialog", "haar混合检测"))
        self.graphicsView_4.setWindowTitle(_translate("Dialog", "LBP人脸检测"))
        self.time_label1.setText(_translate("Dialog","haar人脸检测时间:"))
        self.time_label2.setText(_translate("Dialog","haar眼睛检测时间:"))
        self.time_label3.setText(_translate("Dialog","haar混合检测时间:"))
        self.time_label4.setText(_translate("Dialog","LBP人脸检测时间:"))
        self.time_haarface.setText(_translate("Dialog",""))
        self.time_haareye.setText(_translate("Dialog",""))
        self.time_haarmulti.setText(_translate("Dialog",""))
        self.time_LBPface.setText(_translate("Dialog",""))


    '''
    MessageBox是与各按钮绑定的消息提示框函数，当Dialog中没有加载图片时，
    会弹出提示框，否则会正确地开始图像处理
    '''
    def MessageBox(self):
        sender=self.groupBox.sender()
        print(sender.text())
        print('processlalallala')
        print(type(self.filePath))
        if(self.filePath == ''):
            print('确实文件路径为空')
            dialog=QMessageBox()
            dialog.resize(200,200)
            dialog.setWindowTitle('提示')
            dialog.setText('请先打开一张图片')
            dialog.exec_()
        else:
            self.Process(sender.text())

    '''
    人脸检测过程都是Process函数处理，根据不同的按钮(sender),选择不同的检测方式，
    获取用户自己输入的人脸检测参数，最终将检测的人脸或眼睛用矩形绘制出来
    '''
    def Process(self,senderText):
        #重置每种人脸检测方法的时间和人脸检测方法的名字
        if(len(self.detectTime)==4):
            self.detectTime=[]
            self.detectName=[]
            self.groupList={}

        DetectObject = Detection(HAAR_PATH, POSITIVE_FACE, EYE_WITHOUTGLASS, EYE_WITHGLASS, LEFT_EYE, RIGHT_EYE,LBP_PATH)
        #获取scaleFactor：可以决定两个不同大小的窗口扫描之间有多大的跳跃
        if(self.LE_scaleFactor.text()):
            scaleFactor=float(self.LE_scaleFactor.text())
            print(float(scaleFactor))
        else:
            scaleFactor=1.1
        #获取minNeighbors：每一个级联矩形应该保留的邻近个数
        if(self.LE_minNeighbors.text()):
            minNeighbors=int(self.LE_minNeighbors.text())
            print(minNeighbors)
        else:
            print('process5')
            minNeighbors=3

        if(senderText=='Haar人脸检测'):
            self.openfile(self.graphicsView_1)
            print(senderText)
            result=DetectObject.detection(DetectObject.face_cascade(), self.filePath, scaleFactor, minNeighbors)
            faces=result[0]
            time=result[1]
            self.time_haarface.setText(str(round(1000*time,2))+"ms")
            self.detectTime.append(1000 * time)
            self.detectName.append('haar_face')
            self.groupList['haar_face']=1000*time
            self.drawRect(faces,self.scene)

        if(senderText=='Haar眼睛检测'):
            self.openfile(self.graphicsView_2)
            print(senderText)
            result=DetectObject.detection(DetectObject.eye_cascade(), self.filePath, scaleFactor, minNeighbors)
            faces=result[0]
            time = result[1]
            self.time_haareye.setText(str(round(1000*time,2))+"ms")
            self.detectTime.append(1000 * time)
            self.detectName.append('haar_eye')
            self.groupList['haar_eye']=1000*time
            self.drawRect(faces,self.scene)


        if(senderText=='Haar混合检测'):
            self.openfile(self.graphicsView_3)
            print(senderText)
            result=DetectObject.multi_detection(self.filePath,scaleFactor,minNeighbors)
            faces=result[0]
            eyes=result[1]
            time = result[2]
            self.time_haarmulti.setText(str(round(1000*time,2))+"ms")
            self.detectTime.append(1000 * time)
            self.detectName.append('haar_multi')
            self.groupList['haar_multi']=1000*time
            self.drawRect(faces, self.scene)
            #在人脸区域中再绘制检测到的眼睛
            for(x,y,w,h) in faces:
                for(ex,ey,ew,eh) in eyes:
                    self.scene.addRect(QRectF(ex+x,ey+y,ew,eh),Qt.green)
                    print(x,y,w,h)
                    print(ex,ey,ew,eh)

        if(senderText=='LBP人脸检测'):
            self.openfile(self.graphicsView_4)
            print(senderText)
            result=DetectObject.detection(DetectObject.LBP_cascade(), self.filePath, scaleFactor,minNeighbors )
            faces=result[0]
            time = result[1]
            self.time_LBPface.setText(str(round(1000*time,2))+"ms")
            self.detectTime.append(1000 * time)
            self.detectName.append('LBP_face')
            self.groupList['LBP_face']=1000*time
            self.drawRect(faces,self.scene)

    '''
    timeDict函数是一个获取各种人脸检测方式在不同的scaleFactor大小下检测时间的字典
    dict中每一项时一个list
    '''
    def timeDict(self):
        print('timeDict')
        DetectObject = Detection(HAAR_PATH, POSITIVE_FACE, EYE_WITHOUTGLASS, EYE_WITHGLASS, LEFT_EYE, RIGHT_EYE,LBP_PATH)
        print('DetectObject')
        dict={}
        dict['haar_face']=str(DetectObject.scaleChange(DetectObject.face_cascade(),self.filePath))
       # print('haar_face'+dict['haar_face'])

        dict['haar_eye']=str(DetectObject.scaleChange(DetectObject.eye_cascade(),self.filePath))
      #  print('haar_eye' + dict['haar_eye'])

        dict['haar_multi']=str(DetectObject.scaleChange_multi(self.filePath))
      #  print('haar_multi' + dict['haar_multi'])

        dict['LBP_face']=str(DetectObject.scaleChange(DetectObject.LBP_cascade(),self.filePath))
       #  print('LBP_face' + dict['LBP_face'])

        return dict

    def DrawResult(self):
        print('DrawResult')
        dict=self.timeDict()
        print(' dict=self.timeDict()')
        result=DrawTable(dict)
        print('result=DrawTable(self.timeDict())')
        #print(self.detectTime)
        result.drawLineChart(self.detectName,self.groupList)
        #result.DrawHistograms(self.detectTime)


#在检测出人脸的区域绘制矩形
    def drawRect(self,faces,scene):
        for (x, y, w, h) in faces:
            pe = QPalette()
            pe.setColor(QPalette.WindowText, Qt.blue)
            self.scene.setPalette(pe)
            scene.addRect(QRectF(x, y, w, h),Qt.blue)



    def openfileDialog(self):
        dlg=win32ui.CreateFileDialog(1) #1表示打开文件对话
        dlg.SetOFNInitialDir('Y:/Images')  #设置打开文件对话框的初始目录
        dlg.DoModal()
        self.filePath = dlg.GetPathName()  # 获取选择的文件路径及名称
        print("文件路径"+self.filePath)
        self.openfile(False)
        self.detectTime = []
        self.detectName=[]
        self.groupList={}


    def openfile(self,graphicsView=False):
        original=cv2.imread(self.filePath)
        if(original==None):
            print("original是None啊")
            self.filePath==[]
        else:
            #将图像加载到graphicsView中
            pixmap = QPixmap()
            pixmap.load(self.filePath)
            print("hahahahah"+self.filePath)
            if(graphicsView==False):
                graphicsView=self.graphicsView_1
            self.scene = QGraphicsScene(graphicsView)
            item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(item)
            self.scene.addText(graphicsView.windowTitle(), QFont("Roman times", 10, QFont.Bold))
            graphicsView.setScene(self.scene)
            return self.scene


if __name__=='__main__':

    app=QApplication(sys.argv)
    Form=QMainWindow()
   # Form=QWidget()
    ui=Ui_Dialog()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec())