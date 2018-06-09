

# 整数  没有限制
print(123)
print(0)
print(-1234567)
print(2147483648214)

# 指数写法  科学计数法
print(1.234e10)
# 0-9 ab c d e f  16进制数
print(0xabcdef)

# 汉字的ASCII码
print(0x4E00)

# 浮点数
print(1.0)
print(-123.456)

print(9.87654321e-10)

# 字符串 String  单引号和双引号都可以
print('你好')
print("你好")
print("'")   # 输出单引号
print('"')
print('\'\"')  #输出单引号和双引号
print('\\')
print('\\t\\') #  输出\tab\
print(r'\\t\\') # r 里面的\不是转义的作用
print(r'\\')
print('百日依山尽，\n黄河入海流')   # 英文不建议这样做

# 换行的建议写法
print('''百日依山尽，
黄河入海流''')

# 布尔类型
print(True)
print(False)

print(1<2)
print(1>2)

print(True and True) # 与运算符  or 是或符合
print(False and False) # 与运算符
print(True and False) # 与运算符
print(False and True) # 与运算符

print(not True) # 非运算
print(None)  # 空值

# score=input('input student\'s score:')

# 循环的分支机构
# passed = (score>=60)
passed = False

# 四个空格相当于大括号

if passed:
    print('passed...')
else:
    print('failed...')
    print('test...')

