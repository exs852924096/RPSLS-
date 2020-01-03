#coding:gbk
"""
����ʵ�ֶԡ����������Ľֵ����ı��������ϵ����ȡ��������Gelphi����������ϵ���ӻ��������������������ϵͼ�ס�
���ߣ�������
2019/12/28
"""

import jieba
import os,sys
from jieba import posseg

names={} #�����ֵ�
relationships={} #��ϵ�ֵ�
linenames=[] #ÿ���������ϵ�б�
#�ִʷ���
with open("���������Ľֵ�.txt","r") as files:
     for line in files.readlines():
         pos=posseg.cut(line)#�ִʷ��ش���
         linenames.append([])#Ϊ�¶�ȡ��һ����������ϵ
         for i in pos:
             if i.flag!="nr" or len(i.word)<2:
                 continue #�ִʳ���С��2 ����Բ�Ϊnrʱ����ӰƬ������������޹�
             else:
                  linenames[-1].append(i.word)
             if names.get(i.word) is None:
                names[i.word]=1
                relationships[i.word]={}
             else:
                  names[i.word]+=1  #������ִ���+1
#���������ϵ
for line in linenames:
    for name1 in line:
        for name2 in line:
            if name1==name2:
                 continue
            elif relationships[name1].get(name2) is None:
                 relationships[name1][name2]=1  #���������һ�ι�ͬ���� ��ʼ������
            else:
                 relationships[name1][name2]+=1    #�������ﹲͬ���� ��ϵ+1
#дcsv�ļ� ��������ͼʹ��
with open("���������Ľֵ�_node.csv","w") as file1:  #����Ȩ��(�ڵ�)
     file1.write("id label weight\r\n")
     for name,times in names.items():
         file1.write(name+" "+name+" "+str(times)+"\r\n")

with open("���������Ľֵ�_edge.csv","w") as file2:    #�����ϵ��(��)
     file2.write("source target weight\r\n")
     for name,edge in relationships.items():
         for x,y in edge.items():
             if y>1:
                file2.write(name+" "+x+" "+str(y)+"\r\n")#ͳ�����ֵĳ��ִ���

