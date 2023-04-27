# nmu1 = int(input("请输入第一个数字"))
# nmu2 = int(input("请输入第二个数字"))
# a = input("请输入+-*/中任意值")
#
# if a == "+":
#     print(nmu1+nmu2)
# elif a == "-":
#     print(nmu1-nmu2)
# elif a == "*":
#     print(nmu1*nmu2)
# elif a== "/":
#     print(nmu1/nmu2)

# num1 = int(input("请输入任意整数"))
# if num1 % 2 ==0:
#     print("oushu")
# else:
#     print("jishu")

# 判断正负数
# num1 = int(input("请输入任意整数"))
# if num1 >=0:
#     print("正数")
# else:
#     print("负数")

# 通过 input 输入⼀个数 ，编写代码判断该数是否在 0 到 120 之间 。
# num1 = int(input("请输入"))
# if num1 > 0 and num1 < 120:
#     print("zheng")

# name = input("请输入账号")
# password = input("请输入密码")
# if  name == "itcast" and password == "123456":
#     print("chenggong")
# else:
#     print("shibai")

# age =int(input("请输入"))
# if age < 10:
#     print("小孩")
# elif age > 10 and age < 20:
#     print("小朋友")
# elif age > 20:
#     print("老人")
# else:
#     print("cuowo")

# name = input("请输入")
# if name == "tom":
#     age = int(input("输入"))
#     if age >= 30:
#         print("大叔")
#     elif age <= 30:
#         print("小弟")
# else:
#     print("错误")

# 导入生成随机数的模块
# import random
# # 生成从 10 到 20 之间的一个随机整数
# pc = random.randint(1,3)
# a = None
# if pc == 1:
#     a = "石头"
# elif pc == 2:
#     a = "剪刀"
# else:
#     a = "布"
#
# # player 代表我，具体值从键盘输入
# player = input("请输入石头剪刀布")
# if (player == "石头" and a == "剪刀" ) or (player == "剪刀" and a == "布" ) or (player == "布" and a == "石头" ):
#     print(("电脑出%s , 我出%s,我赢") % ( a,player))
# elif a == player:
#     print("电脑出的%s, 我出的%s, 平局" % (a, player))
# else:
#     print("电脑出的%s, 我出的%s, 我输了" % (a, player))



# length = int(input("请输入身高"))
# if length <= 150:
#     print("进度")
# else:
#     print("买票")

# import random
# num = random.randint(0,999)
# print(num)
# if num > 0  and num <= 9:
#     print("毫米")
# elif num > 10  and num <= 99:
#     print("厘米")
# elif num > 100  and num <= 999:
#     print("分米")