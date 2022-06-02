

# for循环
"""
for 循环变量 in 序列
代码块
"""

# 需求：循环字符串abcdefg中的每个字符
for y in "abcdefg":
    print(y)

print("==================================")
# while循环
"""
while 条件语句：
代码块
"""

# 需求：打印1-5的数
a = 1
while a <= 5:
    print("a的值是", a)
    a = a + 1
    # a += 1


print("================================")
# 计算1-100内所有数的和
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
    print(sum)

# 打印1-10的数字
for a in range(1,10,1):
    print(a)

