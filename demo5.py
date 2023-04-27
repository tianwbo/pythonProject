# def hello():
#     print("nihao")
#     print("nihao")
#     print("nihao")
#
#
# hello()

# 定义一个函数，名字叫 my_func1
# def my_func1():
#     print("*" * 20)
#
#
# my_func1()


# 、形参和实参
# 定义一个函数，名字叫 my_func2，有一个参数 num1；
# 调用 my_func2 时，num1 为 1，输出个*号，num1 为 5，输出 5 个*号；
# 举例：调用函数 my_func2(3)应该输出如下结果:

# def my_func2(num1):
#     result = "*" * num1
#     print(result)
#
#
# my_func2(3)
#
# def my_sum2(num1, num2):
#     result = num1 + num2
#     return result # return 后面的代码，将不会被执行
#     print("test")
#     a = my_sum2(5, 9)
#     print(a)
#


#
# # 返回两个函数中最大的
# def my_max(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# c  = my_max(4,55)
# print(c)
#
#
# # 定义⼀个函数，有两个参数，start 和 stop，start 代表开始范围，stop 代 表终止范围，求这个范围中所有整数相加的和
# def my_sum1(strat,stop):
#     sum =0
#     a = strat
#     while a <= stop:
#         sum += a
#         a += 1
#     return sum
#
#
# print(my_sum1(2,6))

# def my_squar(height,width):
#     return height * width
#
#
# print(my_squar(3, 4))
#
#
#
#
# def my_func(num1,num2):
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False
#
#
# print(my_func(8, 4))
# print(my_func(9, 4))


# # 函数------嵌套调⽤
# def test1():
#     print("我是 test1")
# def test2(): # 先执行函数 test1 的代码 test1()
#         test1 #函数执行完毕后，再执行下面代码
#         print("我是 test2")
#
#
# test2()

# 全局和局部变量
#
# def my_func1():
#     a = 10
#
# def my_func2():
#     a = 20
#     my_func1() #调用 my_func2 函数，不会影响 a 的值
#     print("a = %d" % a)
#
#
# my_func2()


# 定义一个全局变量 name=”张三”, 定义一个函数 my_test1, 在函数 my_test1 内部 修改全局变量 name 的值为”李四”

# name = "张三"
# def my_test1():
#     global name
#     name = "lisi"
#
#
# my_test1()
# print(name)

# 定义一个函数，参数为列表类型，调用函数过后，删除列表所有值
# list1 = [2, 5, 3]
# def my_sun1(list1):
#     list1.clear()
#
#
# my_sun1(list1)
# print(list1)



