#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：罗梁铭
日期：2019/11/20
"""

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(player_chioce):
    """
    将游戏对象对应到不同的整数
    """
    if player_chioce=="石头":
       print(0)
    elif player_chioce=="史波克":
	     print(1)
    elif player_chioce=="纸":
	     print(2)
    elif player_chioce=="蜥蜴":
	     print(3)
    elif player_chioce=="剪刀":
	     print(4)
player_chioce=input("请输入你的选择:")	          
name_to_number(player_chioce)

import random
number=random.randint(0,4)
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
       return("石头")
    if number==1:
       return("史波克")
    if number==2:
       return("纸")
    if number==3:
       return("蜥蜴")
    if number==4:
       return("剪刀")
comp_number=number_to_name(number)
print("欢迎使用RPSLS游戏")
print("----------------")
print("计算机的选择:%s"%comp_number)

print("您的选择:",player_chioce)	      
	   
def rpsls(player_choice,comp_number):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
win_list=[["剪刀","纸"],["纸","石头"],["石头","剪刀"],["石头","蜥蜴"],["蜥蜴","史波克"],["史波克","剪刀"],["剪刀","蜥蜴"],["蜥蜴","纸"],["纸","史波克"],["史波克","石头"]]
str=["石头","史波克","纸","蜥蜴","剪刀"]
if player_chioce in str:
   if player_chioce==comp_number:
	   print("您和计算机出的一样呢")
   elif [player_chioce,comp_number] in win_list:
		  print("您赢了")
   else:
		  print("计算机赢了")
else:
    print("Error: No Correct Name")
rpsls(player_chioce,comp_number)
