
# 实例：创建学生类，要求属性有：姓名和年级；方法有：学习的方法，打印学生的上课情况
class Students():

    name = ""
    grade = ""

    # 申明构造方法：__init__()
    def __init__(self):
        print("此方法会被自动执行")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s1 = Students()
s1.name = '张三'
s1.grade = '5'
# print(s1.study())

s2 = Students()
s2.name = '李四'
s2.grade = '1'
# print(s2.study())


# 以上需求使用构造方法去实现
class Students1():

    name = ""
    grade = ""

    # 申明构造方法：__init__()
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        print("此方法会被自动执行")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s3 = Students1('王五',6)
s3.study()

# 需求：实现连接数据库
"""
1.定义连接数据库的类
2.必须和数据库建立连接，使用构造方法是最合适的
3.进行各种的方法调用

"""

