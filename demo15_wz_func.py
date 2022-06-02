
# 函数：位置参数

def add (x,y):
    return x + y

print(add(3,4))
print(add('hello','world'))
# print(add(3))
# print(add(3,4,5))
# print(add())

# 关键字参数
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z

print(student_lesson(grade=2,subject='语文'))

# 用处：实现一个函数，参数特别多
# connect(host='localhost',username='root',password='root',database,port,commit)

# 默认参数：其中某个参数会有默认值，带有默认值得参数放在最后面。
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info

print(study_language('张三','java'))
print(study_language('李四','python'))
print(study_language('王五'))

