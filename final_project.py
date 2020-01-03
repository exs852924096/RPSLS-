#coding:gbk
"""
程序：实现对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化，生成如下类似人物关系图谱。
作者：罗梁铭
2019/12/28
"""

import jieba
import os,sys
from jieba import posseg

names={} #姓名字典
relationships={} #关系字典
linenames=[] #每段内人物关系列表
#分词方法
with open("黎明破晓的街道.txt","r") as files:
     for line in files.readlines():
         pos=posseg.cut(line)#分词返回词性
         linenames.append([])#为新读取的一段添加人物关系
         for i in pos:
             if i.flag!="nr" or len(i.word)<2:
                 continue #分词长度小于2 或词性不为nr时则与影片所需分析人物无关
             else:
                  linenames[-1].append(i.word)
             if names.get(i.word) is None:
                names[i.word]=1
                relationships[i.word]={}
             else:
                  names[i.word]+=1  #人物出现次数+1
#分析人物关系
for line in linenames:
    for name1 in line:
        for name2 in line:
            if name1==name2:
                 continue
            elif relationships[name1].get(name2) is None:
                 relationships[name1][name2]=1  #两个人物第一次共同出现 初始化次数
            else:
                 relationships[name1][name2]+=1    #两个人物共同出现 关系+1
#写csv文件 用于网络图使用
with open("黎明破晓的街道_node.csv","w") as file1:  #人物权重(节点)
     file1.write("id label weight\r\n")
     for name,times in names.items():
         file1.write(name+" "+name+" "+str(times)+"\r\n")

with open("黎明破晓的街道_edge.csv","w") as file2:    #人物关系边(边)
     file2.write("source target weight\r\n")
     for name,edge in relationships.items():
         for x,y in edge.items():
             if y>1:
                file2.write(name+" "+x+" "+str(y)+"\r\n")#统计名字的出现次数

