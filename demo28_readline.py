
# 读取文件

# 1）打开文件： open(filename,mode)  filename代表的是文件名，mode:读写模式
f = open('a.txt','r')


# 2）读取文件：read()
while True:
    line = f.readline()
    print(line,end='')
    if not line:
        break

# 3）关闭文件：
f.close()
