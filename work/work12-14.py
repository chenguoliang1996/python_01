# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
astr = "fdssadf sdfsdfsdf 43612834fskdlfhsak"
zf = 0
kg = 0
sz = 0
other = 0
for x in astr:
    if x.isalpha():   # 判断字符
        zf +=1
    elif x.isdigit():
        sz += 1
    elif x.isspace():
        kg += 1
    else:
        other += 1
print("字符：", zf)
print("数字：", sz)
print("空格：", kg)
print("其他：", other)

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。


# 14. 题目：打印出如下图案（菱形）:
num = 5
x = num - 1
for n in range (1,5):
    space = " " * (x-n)
    star = "*" * (2*n-1)
    print(space + star)
for n in range(1,4):
    space = n * " "
    star = (7 - 2 * n) * "*"
    print(space + star)