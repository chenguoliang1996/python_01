
# 序列的通用操作

# 1.索引 - 列表，序列，元祖， 字符串
lst = ['red', 'hello', 2, 3.5]
print(lst[1])
print(lst[-3])

tp = ('red', 'hello', 2, 3.5)
print(tp[1])
print(tp[-1])

my_str = "redhello2"
print(my_str[1])
print(my_str[-1])

# 2.序列的切片：seq[start:end:step],start代表开始位置，默认为0.
# end代表结束位置，不包括该位置，不填写代表列表长度。step代表步长，默认是1
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:6:1])

print(lst5[:2:])
print(lst5[::2])
print(lst5[1::])

# 列表中有10个元素，让你取出其中奇数个数的元素
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[::2])

# 列表相加，相乘
alst = [1,2]
blst = [3,4]
clst = alst + blst
print(clst)
astr = 'hello'
bstr = 'python'
print(astr + bstr)

dlst = alst * 2
print(dlst)

elst = [None] * 3
print(elst)

print("=====================")
print("=" * 30)

# 检查元素：in,针对的是列表，字符串，元祖
lst6 = ['red','green','blue','black','gold','orange']
print('gold' in lst6)
print('gold1' in lst6)

# 序列中的方法:list()
print("=" * 50)
klst = list()
print(klst)
cstr = "abc"
mlst = list(cstr)
print(mlst)

nlst = [1,2,3]
dstr = str(nlst)[1::2]
# for i in dstr:
#     print(i)
print(dstr)

#
lst7 = ['red','green','blue','black','gold','orange']
for x in lst7:
    print(x,end=' ')
print()

# 循环序列中的索引和值
for index,vls in enumerate(lst7):
    print(index,'=========',vls)
