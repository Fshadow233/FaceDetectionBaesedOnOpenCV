# -*- coding: utf-8 -*-

import cv2
import os

class Detection:
    def __init__(self,PATH,POSITIVE_FACE,EYE_WITHOUTGLASS,EYE_WITHGLASS,LEFT_EYE,RIGHT_EYE,LBP_PATH):
        # 分类器的路径
        self.PATH = PATH
        self.POSITIVE_FACE = POSITIVE_FACE
        self.EYE_WITHOUTGLASS = EYE_WITHOUTGLASS
        self.EYE_WITHGLASS = EYE_WITHGLASS
        self.LEFT_EYE = LEFT_EYE
        self.RIGHT_EYE = RIGHT_EYE
        self.LBP_path=LBP_PATH

    def face_cascade(self):
        return self.PATH + self.POSITIVE_FACE

    def eye_cascade(self):
        return self.PATH + self.EYE_WITHOUTGLASS

    def lefteye_cascade(self):
        return self.PATH+self.LEFT_EYE

    def righteye_cascade(self):
        return self.PATH+self.RIGHT_EYE

    def LBP_cascade(self):
        return self.LBP_path

    #每种分类器单一检测
    def detection(self,filePath,imgPath,scaleFactor,minNeighbors):
        img=cv2.imread(imgPath)
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像灰度化
        cascade=cv2.CascadeClassifier(filePath)
        e1 = cv2.getTickCount()  # 获取当前时间戳
        faces = cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
        e2 = cv2.getTickCount()  # 获取当前时间戳
        time_facedetect = (e2 - e1) / cv2.getTickFrequency()  # 计算人脸检测时间
        print("time of face detection:" + str(time_facedetect) + "\n")
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #返回检测到的人脸/眼睛和检测时间
        return faces,time_facedetect



    #混合检测
    def multi_detection(self, imgPath, scaleFactor,minNeighbors):
        img=cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像灰度化
        face_cascade=cv2.CascadeClassifier(self.face_cascade())
        e1 = cv2.getTickCount()  # 获取当前时间戳
        faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
        e2 = cv2.getTickCount()  # 获取当前时间戳
        time_facedetect = (e2 - e1) / cv2.getTickFrequency()  # 计算人脸检测时间
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_img = img[y:y + h, x:x + w]
            eye_cascade=cv2.CascadeClassifier(self.eye_cascade())
            e1 = cv2.getTickCount()
            eyes=eye_cascade.detectMultiScale(roi_gray)
            #eyes =  eye_cascade.detectMultiScale(roi_gray)
            e2 = cv2.getTickCount()
            time_eyedetect = (e2 - e1) / cv2.getTickFrequency()  # 计算眼睛检测时间
           # print("time of eye detection:" + str(time_eyedetect) + "\n")
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return faces,eyes,time_facedetect+time_eyedetect


    ##这里写一个函数 测试所有检测方法在不同检测窗口scaleFactor和minNeighbors的大小的情况下的检测事件
    #以此生成所有人脸检测方法的时间走向图
    # #那么第一个函数是以scaleFactor为参数,minNeighbors默认为3
    #啦啦啦，当然这个函数只能是Haar人脸检测、LBP人脸检测、haar眼睛检测，不能是混合加测方法
    #参数详解 filePath：分类器的路径   imgPath：图像的路径
    def scaleChange(self,filePath,imgPath):
        img=cv2.imread(imgPath)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_cascade=cv2.CascadeClassifier(filePath)
        times=[]
        scale=1.1
        while scale<2:
            e1 = cv2.getTickCount()  # 获取当前时间戳
            face_cascade.detectMultiScale(gray, scale, 3)
            e2 = cv2.getTickCount()  # 获取当前时间戳
            time= (e2 - e1) / cv2.getTickFrequency()  # 计算人脸检测时间
           # print('时间'+str(time))
            times.append(1000*time)
            scale=scale+0.1
        print(times)
        return times

    #scaleChange_multi是在不同检测窗口下获取混合检测所需要的时间
    #返回值是一个时间的list
    def scaleChange_multi(self,imgPath):
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像灰度化
        face_cascade = cv2.CascadeClassifier(self.face_cascade())
        times=[]
        scale=1.1
        while scale<2:
            e1 = cv2.getTickCount()  # 获取当前时间戳
            faces = face_cascade.detectMultiScale(gray, scale, 3)
            e2 = cv2.getTickCount()  # 获取当前时间戳
            time_facedetect = (e2 - e1) / cv2.getTickFrequency()  # 计算人脸检测时间
          #  print("time of face detection:" + str(time_facedetect) + "\n")
            for (x, y, w, h) in faces:
               # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]       #获取检测到的人脸感兴趣区域
                eye_cascade = cv2.CascadeClassifier(self.eye_cascade())  #获取眼睛分类器
                e1 = cv2.getTickCount()
                eye_cascade.detectMultiScale(roi_gray)
                e2 = cv2.getTickCount()
                time_eyedetect = (e2 - e1) / cv2.getTickFrequency()  # 计算眼睛检测时间
             #   print("time of eye detection:" + str(time_eyedetect) + "\n")
            time=time_facedetect+time_eyedetect
            print('混合时间' + str(time))
            times.append(1000*time)
            scale=scale+0.1
        return times


