# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
# sum1 = 0
# sum2 = 0
# for x in range(1,101):
#     if x % 2 == 0:
#         sum1 += x
#     else:
#         sum2 += x
# print(abs(sum1 - sum2))

# sum1 = 0
# sum2 = 0
# x = 1
# while x <= 100:
#     if x % 2 == 0:
#         sum1 += x
#     else:
#         sum2 += x
#     x += 1
# print(sum1 - sum2)

# 5. 求1+2+3+...+100的和
# sum = 0
# for x in range(1,101,1):
#     sum += x
# print(sum)
#
# sum = 0
# x = 1
# while x <= 100:
#     sum += x
#     x += 1
# print(sum)

# 6. 判断一个数n能同时被3和5整除
n = input("请输入一个整数：")
if int(n) % 3 == 0 and int(n) % 5 == 0:
    print(n, "能能同时被3和5整除")
else:
    print(n, "不能能能同时被3和5整除")


