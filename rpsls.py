#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019/11/20
"""

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(player_chioce):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if player_chioce=="ʯͷ":
       print(0)
    elif player_chioce=="ʷ����":
	     print(1)
    elif player_chioce=="ֽ":
	     print(2)
    elif player_chioce=="����":
	     print(3)
    elif player_chioce=="����":
	     print(4)
player_chioce=input("���������ѡ��:")	          
name_to_number(player_chioce)

import random
number=random.randint(0,4)
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
       return("ʯͷ")
    if number==1:
       return("ʷ����")
    if number==2:
       return("ֽ")
    if number==3:
       return("����")
    if number==4:
       return("����")
comp_number=number_to_name(number)
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("�������ѡ��:%s"%comp_number)

print("����ѡ��:",player_chioce)	      
	   
def rpsls(player_choice,comp_number):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
win_list=[["����","ֽ"],["ֽ","ʯͷ"],["ʯͷ","����"],["ʯͷ","����"],["����","ʷ����"],["ʷ����","����"],["����","����"],["����","ֽ"],["ֽ","ʷ����"],["ʷ����","ʯͷ"]]
str=["ʯͷ","ʷ����","ֽ","����","����"]
if player_chioce in str:
   if player_chioce==comp_number:
	   print("���ͼ��������һ����")
   elif [player_chioce,comp_number] in win_list:
		  print("��Ӯ��")
   else:
		  print("�����Ӯ��")
else:
    print("Error: No Correct Name")
rpsls(player_chioce,comp_number)
