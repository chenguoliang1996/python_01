# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# x = input("请输入一个整数：")
# if 1 <= int(x) <= 100:
#     print(x)
# else:
#     print("不是")

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
# lst = []
# x = input("输入x:")
# y = input("输入y:")
# z = input("输入z:")
# lst.append(x)
# lst.append(y)
# lst.append(z)
# print(lst)
# lst.sort()
# print(lst)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
score = int(input("请输入你的分数："))
if score >= 90:
    print("A")
elif 60 <= score <= 89:
    print("B")
else:
    print("C")

