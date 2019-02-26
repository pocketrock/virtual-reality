#!/usr/bin/python
# -*- coding: GBK -*-
import re
from numpy import *
import operator
from os import listdir
import xlrd
from xlwt import *
import xlutils.copy
from xlutils.copy import copy
import os
import numpy as np
import pandas as pd
import xlwt
#print(first_line[0])
#print(first_line[1])
#print(first_line[2])
#print(first_line[3])


def quww(wwww,kkkkk):

      datafile = '../data/change-trial/'+str(kkkkk)+".txt"

      f = open(datafile, 'r',encoding='GBK')
      n=0
      lines = f.readlines()
      for line in lines:
              n=n+1
     # print(n)
      first_line = lines[0]

      first_line = first_line.split()
      listVal = [];
      for i in range(12):
          listVal.append(0);
     # ewqe=0
      #print ( listVal)
      for i0 in range (4):

           if first_line[i0] == str(wwww):
               for j in range (n):
                     tmp=lines[j].split()
                     if len(tmp):
                       for kk in range (32):

                           if str(i0 * 32 + kk)+ "出现物体" == ("".join(tmp[0])):

                                    gggg =tmp[0] + " " + tmp[1] + " " + tmp[2] + " " + tmp[3] + " " + tmp[4]
                                    print(gggg)
                                    listVal[0]=tmp[1]
                                    listVal[1] = tmp[2]
                                    listVal[2] = tmp[3]
                                    listVal[3] = tmp[4]

                                    listVal[4] = tmp[1]
                                    listVal[5] = tmp[2]
                                    listVal[6] = tmp[3]
                                    listVal[7] = tmp[4]
                                    #print(listVal)
                           if str(i0 * 32 + kk + 1) + "替换物体" == ("".join(tmp[0])):

                                    gggg = tmp[0] + " " + tmp[1] + " " + tmp[2] + " " + tmp[3] + " " + tmp[4]
                                    print(gggg)
                                    listVal[0] = listVal[4]
                                    listVal[1] = listVal[5]
                                    listVal[2] = listVal[6]
                                    listVal[3] = listVal[7]

                                    listVal[4] = tmp[1]
                                    listVal[5] = tmp[2]
                                    listVal[6] = tmp[3]
                                    listVal[7] = tmp[4]
                                    print(listVal)
                                    for i in range (0,4):
                                          if (int(listVal[i+4])-int(listVal[i]))!=0:
                                               print(i)
                                               print(listVal[i + 8])
                                               rb = xlrd.open_workbook('../tmp/shichang.xls', formatting_info=True)

                                               wb = xlutils.copy.copy(rb)
                                               ws = wb.get_sheet(0)

                                               ws.write(wwww * 32 + kk + 1, 2 * kkkkk - 1, ("".join(tmp[0]))[:-4])  # 向第1行第1列写入获取到的值

                                               ws.write(wwww * 32 + kk + 1, 2 * kkkkk,listVal[i + 8] )
                                               wb.save("../tmp/shichang.xls")


                           if str(i0 * 32 + kk + 1) + "眼动时长" == ("".join(tmp[0])):

                                    gggg=tmp[0]+" "+tmp[1]+" "+ tmp[2]+" "+tmp[3]+" "+tmp[4]
                                    print (gggg)
                                    listVal[8] = tmp[1]
                                    listVal[9] = tmp[2]
                                    listVal[10] = tmp[3]
                                    listVal[11] = tmp[4]





if __name__ == '__main__':

    for ff in range(1,11):
     quww(0,ff)
     quww(1,ff)
     quww(2,ff)
     quww(3,ff)