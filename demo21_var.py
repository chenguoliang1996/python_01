
# 实例变量

# 实例：创建学生类，要求属性有：姓名和年级；方法有：学习的方法，打印学生的上课情况
class Students(object):

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        sex = '男'
        print(name,grade)



s = Students('张三','5年级')
s.name
s.grade

# # 调用的时候有两种方法:
#
# # 1.使用类名去调用
# print(Students.name)
# print(Students.grade)
#
# # 2.使用实例化对象去调用
# s1 = Students()
# # print(s1)
# print(s1.name)
# print(s1.grade)
# # print(s1.study())
