
# 字符串格式化: %s
my_str = "my name is %s" % ('张三')
print(my_str)

# 格式化整数: %d
my_str1 = "张三今年%d岁" % (25)
print(my_str1)

# 格式化浮点数: %f
my_str2 = "一斤苹果%f元" % (3)
print(my_str2)

# 辅助指令： m.n
my_str3 = "一斤苹果%30.8f元" % (3.7)
print(my_str3)

# 显示左对齐：  -
my_str4 = "一斤苹果%-30.8f元" % (3.7)
print(my_str4)

# 数字前面显示+： +
my_str5 = "一斤苹果%+-30.8f元" % (3.7)
print(my_str5)

# 数字前面显示空格
my_str6 = "一斤苹果%- 30.8f元" % (3.7)
print(my_str6)

# 数字前面显示0: 0
my_str7 = "一斤苹果%030.8f元" % (3.7)
print(my_str7)

# 使用format去格式化："{}".format("字符串")
my_str8 = "张三今年{}岁".format(25)
print(my_str8)

# format格式化两个参数："{} {}".format(参数1，参数2)
my_str9 = "今天星期{}，张三买了{}斤苹果".format('一', 3)
print(my_str9)

# format的位置参数："{0}{2}{1}{3}".format(第一个，第二个，第三个，第四个)
my_str10 = "今天星期{0}，张三买了{1}斤苹果".format('一', 5)
print(my_str10)

# format的关键字参数："{x}{y}".format(x='hello',y='world')
my_str11 = "今天星期{x}，张三买了{y}斤苹果".format(x='一', y=5)
print(my_str11)

# 位置参数和关键字参数结合使用:"{0}{y}".format('hello',y='world')
my_str12 = "今天星期{0}，张三买了{y}斤苹果".format('一', y=5)
print(my_str12)
