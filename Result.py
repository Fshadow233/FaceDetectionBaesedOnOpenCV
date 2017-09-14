# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import  pylab as pl
from matplotlib import  pyplot as plt
from pylab import *
from matplotlib.legend_handler import HandlerLine2D
#设置字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


class DrawTable:
    def __init__(self,timeDict):
        self.timeDict=timeDict

    #将从dict中获取的str类型的value转换为list
    def strToList(self, files):
        files=files.replace('[', '').replace(']', '')
        list=files.split(',')
        return list

    #DrawTable绘制人脸检测随scale参数变化的检测时间的折线图
    def drawLineChart(self,xticks,groupList):

        timeList1=self.strToList(self.timeDict.get('haar_face'))
        print('timeList1'+str(timeList1))
        timeList2=self.strToList(self.timeDict.get('haar_eye'))
        print('timeList2'+str(timeList2))
        timeList3=self.strToList(self.timeDict.get('haar_multi'))
        print('timeList3'+str(timeList3))
        timeList4=self.strToList(self.timeDict.get('LBP_face'))
        print('timeList4'+str(timeList4))
        x_scale=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
        #添加轴标题以及轴坐标限度
        plt.subplot(121),plt.title(u'人脸检测时间随scale参数的变化'),plt.xlabel(u'scale'),plt.ylabel(u'time/ms'),

        #绘制折线图 参数一为横坐标，参数二为纵坐标 参数三为绘制方式及线条颜色
        plot1,=plt.plot(x_scale, timeList1,'b',label='line1')
        plot2,=plt.plot(x_scale,timeList2,'g-.',label='line1')
        plot3,=plt.plot(x_scale,timeList3,'r--')
        plot4,=plt.plot(x_scale, timeList4,'c:')
        
        # 绘制散点图
        plt.plot(x_scale, timeList1, 'ob')
        plt.plot(x_scale, timeList2, 'og')
        plt.plot(x_scale, timeList3, 'or')
        plt.plot(x_scale, timeList4, 'oc')
        #为每个子图添加说明 第三个参数:位置 :'best’‘upper right’, ‘upper left’, ‘center’, ‘lower left’, ‘lower right’.
        pl.figlegend([plot1, plot2, plot3, plot4], ['face', 'eye', 'multi', 'LBP'], 'upper right')

        if(len(xticks)==4):
            n = np.array([0, 1, 2, 3])
            plt.subplot(122),plt.bar(range(4),[groupList.get(xtick, 0) for xtick in xticks],width=0.5,alpha=0.5),plt.xlabel('人脸检测'),plt.ylabel('time/ms'),plt.xticks(range(4), xticks),plt.title('时间对比')
        else:
            pass

      #  plt.legend(handler_map={plot1: HandlerLine2D(numpoints=4)})
        #添加标注

        plt.show()



    '''
    #DrawHistograms函数是绘制不同检测方式在相同检测参数情况下时间对比的直方图
    def DrawHistograms(self,timeList):

        print('aaaa')
        n = np.array([0, 1, 2, 3])
        print(timeList)
       # plt.bar(['haar_face','haar_eye','haar_multi','LBP_face'],timeList,width=0.8,alpha=0.5)

        plt.bar(n,timeList,width=0.8,alpha=0.5)
        plt.xlabel('人脸识别')
        plt.ylabel('time/ms')
        print('eeee')
        plt.show()
        print('ffff')


        # DrawTable绘制人脸检测随scale参数变化的检测时间的折线图
    def drawLineChart(self):
        #获取每种检测方法的时间表
        timeList1 = self.strToList(self.timeDict.get('haar_face'))
        print('haar_face' + str(timeList1))
        timeList2 = self.strToList(self.timeDict.get('haar_eye'))
        print('haar_eye' + str(timeList2))
        timeList3 = self.strToList(self.timeDict.get('haar_multi'))
        print('haar_multi' + str(timeList3))
        timeList4 = self.strToList(self.timeDict.get('LBP_face'))
        print('LBP_face' + str(timeList4))

        #scale参数值
        x_scale = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
        # 添加轴标题以及轴坐标限度
        pl.title(u'人脸识别时间随scale参数的变化')
        plt.xlabel(u'scale')
        plt.ylabel(u'time/ms')

        # 绘制折线图
        plot1, = pl.plot(x_scale, timeList1, 'b')
        plot2, = pl.plot(x_scale, timeList2, 'g-.')
        plot3, = pl.plot(x_scale, timeList3, 'r--')
        plot4, = pl.plot(x_scale, timeList4, 'c:')

        # 绘制散点图
        pl.plot(x_scale, timeList1, 'ob'),
        pl.plot(x_scale, timeList2, 'og'),
        pl.plot(x_scale, timeList3, 'or'),
        pl.plot(x_scale, timeList4, 'oc')

        #添加标注
        pl.figlegend([plot1, plot2, plot3, plot4], ['face', 'eye', 'multi', 'LBP'], 'upper right',numpoints=1)
        plt.show()
    '''




