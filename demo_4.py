# 数据类型

# 列表
# list = ["张飞","关羽","刘备","里斯","马五"]
# print(list[0])

# 定义一个空列表变量 向列表内添加 5, 9, 13 这三个数字
# list1 = []
# list1.insert(0,5)
# list1.insert(1,9)
# list1.insert(2,13)
# print(list1)

# # 末尾追加
# list2 = ["a","s"]
# list2.append("wuma")
# print(list2)

# 追加另外一个列表值
# list1 = ["s","d","s2"]
# list2 = ["ww","ss","23d"]
# list2.extend(list1)
# print(list2)

# 定义一个列表变量，内容如下 ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ] 把”刘老二”修改为”周瑜”
# list1 = ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ]
# list1[4] = "周瑜"
# print(list1)
#

# 删除列表数据、
# 定义一个列表
# lis1 = ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ]
# del(lis1[2])  删除索引是2的数据
# lis1.remove( "刘老二")   删除刘老二
# lis1.pop()    删除末尾数据
# lis1.pop(2)   删除索引是2的数据
# lis1.clear()  清空列表
# print(lis1)

# 统计列表中数据的次数
# list1 = [2,22,2,23,13]
# print(list1.count("2"))   统计list1中2的出现次数
# print(list1.index("2",1))   后可加查找的启示位置

# 列表中的排序
# 定义一个列表
# list2 = [25,22,44,1,222]
# 升序排列
# list2.sort()
# 降序排列
# list2.sort(reverse=True)
# 反转位置
# list2.reverse()
# print(list2)


#  定义一个列表变量，内容如下
# list1 = [0, 3, 3, 9, 10 ,3 ,5]
# sum = 0
# for n in list1:
#     sum += 1
# print(sum)

# 定义一个列表变量，内容如下
# list2 = [0, 3, 3, 9, 10 ,3 ,5]
# sum = 0
# for s in  list2:
#     sum += s
# print(sum)

# 拆包
# list1 = ["22","s4","zhangsan"]
# a,b,c = list1
# print(a,b,c)

# # 列表推倒式
# a = [ x for x in range(0,101) if x % 10 == 0]
# print(a)
#
#
# list1 = ["张三","马老五","陈老路","里斯","没啥事是"]
# nmu1 = 0
# for n in list1:
#     if len(n) == 3:
#         nmu1 +=1
# print(nmu1)


# 定义一个列表变量，内容如下
# list1 = ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ]
# if "刘备" in list1:
#     list1.remove("刘备")
#     print(list1)

 # 定义一个列表变量显示列表中最大值
# list2 = [3, 5, 67, 2, 34, 12, 5, 11]
# # print(max(list2))
# sum = 0
# for n in list2:
#     sum += n
# print(sum)
# # print(sum/len(list2))
#

# # 元组
# tuple1 = (23,223,22,22)
# print(tuple1.count(22))
# print(len(tuple1))
# print(max(tuple1))
# print(min(tuple1))


# list1 = ["刘备","关羽","张飞"]
# tuple1 = ("曹操", "周瑜")
# # list1.extend(tuple1)
# # print(list1)
# # list1[3] = "lee"
# # print(list1)
# # print(tuple1)
# a = 0
# for n in tuple1:
#     list1.insert(a,n)
#     a +=1
# print(list1)

# 集合
# set1 = {22,"ss","wushiqu"}
# 集合set1增加值
# set1.add("woyao")
# 集合set1删除最后值
# set1.pop()
# 集合删除ss
# set1.remove("ss")
# 清空集合
# set1.clear()
# print(set1)


# 定义一个空集合变量，通过 input 函数，向集合里输入任意 5 个整数,显示集合中的最小值
# set2 = set()
# a = 0
# while a <5:
#     set2.add(int(input("请输入")))
#     a +=1
# print(min(set2))

# 集合遍历
# set2 = {"sdsa",222,"张飞"}
# for a in set2:
#     print(a)

# 定义一个空集合变量，通过 input 函数，向集合里输入任意 3 个字符串,遍历集合,显示集合中所有的字符串
# set3 = set()
# a =0
# while a < 3:
#     set3.add((input("请输入")))
#     a += 1
# for b in set3:
#     print(b)

# 字典

# dict1 = {"id":10, "name":"周瑜", "age":30}
# dict1 ["sex"] = "nan"
# dict1 ["age"] = 25
# b = dict1 ["name"]
# print(b)
# for a in dict1.items():
#     print(a)
# for a,b in dict1.items():
#     print("键=%s,值=%s" % (a ,str(b)) )

# dict3 = {"a":3,"b":4,"c":5,"d":"sss"}
# for n in dict3:
#     if dict3[n] == "sss":
#         print(n)

# 字符串
# str1 = "hellonihao"
# a = str1[2]
# print(a)

# 遍历字符串
# for a in str1:
#     print(a)
# 得到指定索引位置的字符
# c = str1[2]
# print(c)
# 判断是否都是由字母构成
# str1 = "hellonihwwwao"
# if str1.isalpha():
#     print("shide")
# 判断是否都是数字构成
# str1 = "23323223"
# if str1.isdigit():
#     print("1")
# 计算器
# str1 = input("请输入第一个：")
# str2 = input("请输入第二个：")
# if str1.isdigit() and str2.isdigit():
#     a = int(str1)
#     b = int(str2)
#     print(a + b)
# else:
#     print("错误")

# # 判断字符串是否都是小写
# str1 = "wewewe"
# if str1.islower():
#     print("sd")
# 判断字符串是否都是大写
# str1 = "SSSSDDF2FF"
# if str1.upper():
#     print("2")
#查找字符
# str2 = "p[[]qwqeq23142142sda"
# c = str2.find("q",7)
# print(c)
# 查找字符串并替换
# str3 = " 我们之间的"
# b = str3.replace(" ","2")
# print(b)
# 返回子串在字符串中出现的次数
# str4 = "qwqeq23142142s"
# b  = str4.count("1")
# print(b)
# 大小写转换
# 小写转大写
# str4 = "WEssaqQ"
# c = str4.upper()
# print(c)
# 大写转小写
# str5 = 'AQWEE'
# b = str5.lower()
# print(b)
# 大小写反转
# str8  = "asWE"
# se_c = str8.swapcase()
# print(se_c)
# 去除字符串左侧空格
# str3 = "        women    "
# str4 = str3.lstrip()
# print("'%s'" % str4)
# 去除字符串右侧空格
# str3 = "   women      "
# str4 = str3.rstrip()
# print("'%s'" %  str4)
# # 去除两侧空格
# str5 = "   women      "
# str6 = str5.strip()
# print("'%s'"  % str6)

# # 拆分字符串
# str1 = "ww-ee-cc-eed-eas"
# ayr0 = str1.split()
# print(ayr0)

# 格式化字符串
# id = 1
# name = '刘备'
# weight = 80.2
# tel = '13912345678'
# print("#" * 20 )
# print("编号%06d" % id)
# print("姓名：%s" % name)
# print("体重：%.3f" % weight)
# print("电话：%s" % tel)
# print("#" * 20)

#
# # 字符串切片
# str1 = "我爱 python"
# #   截取从2开始 ~ 6 位置的字符串
# c = str1[2:6]
# #   截取从开始 ~ 6 位置的字符串
# d = str1[:6]
# #   截取从 2 ~ 末尾的字符串
# r = str1[2:]
# #   截取完整的字符串
# e = str1[:]
# #   从索引 1 开始，每隔⼀个取⼀个
# y = str1[1:2]
# #   截取从 2 到末尾 - 1 的字符串
# s = str1[2:-1]
# #   字符串逆序
# t = str1[::-1]
# #   截取字符串末尾两个字符
# o = str1[-2:]
# # print(t)
#
# list2 = ['刘备', '诸葛亮', '曹操', '周瑜', '关羽']
# list2 = list2[::-1]
# print(list2)
# sev = 0
# for n in list2:
#     str1 = n[::-1]
#     list2[sev] = str1
#     sev += 1
# print(list2)




