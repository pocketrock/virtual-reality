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
      #print(first_line[0])
     # print(first_line[1])
     # print(first_line[2])
     # print(first_line[3])
      listVal = [];
      for i in range(129):
          listVal.append(0);
     # print( listVal[125])
      for i0 in range (4):

           if first_line[i0] == str(wwww):
               for j in range (n):
                     tmp=lines[j].split()
                     if len(tmp):
                       for kk in range (32):

                            if str(i0 * 32 + kk + 1) + "正确" == ("".join(tmp[0])):

                               h, m, s =("".join(tmp[1])).strip().split(":")

                               ddd= int(h) * 60000 + int(m) * 1000 + int(s)-3000

                               listVal[(i0 * 32 + kk + 1)]+=1

                               gggg=tmp[0] +" "+str(listVal[(i0 * 32 + kk + 1)])+" "+str(ddd)
                               if listVal[(i0 * 32 + kk + 1)]==1:
                                print(gggg)
                                print(ddd)


                                rb = xlrd.open_workbook('../tmp/excel.xls',formatting_info=True)

                                wb = xlutils.copy.copy(rb)
                                ws = wb.get_sheet(0)

                               # ws.write(wwww*32+kk+1, 2*kkkkk-1, ("".join(tmp[0]))[:-2])  # 向第1行第1列写入获取到的值
                                ws.write(wwww * 32 + kk + 1, 2 * kkkkk - 1, ("".join(tmp[0])))
                                ws.write(wwww*32+kk+1, 2*kkkkk, str(ddd))
                                wb.save("../tmp/excel.xls")


                           # if str(i0*32+kk+1)+"错误" == ("".join(tmp[0])):

                                # print(tmp[0] + tmp[1])


if __name__ == '__main__':
    for ff in range(1,11):
     quww(0,ff)
     quww(1,ff)
     quww(2,ff)
     quww(3,ff)