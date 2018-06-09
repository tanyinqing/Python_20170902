s1='A'
s2='-'
print(ord(s1))  # 单一的字符输出ACII值
print(ord(s2))
print(0x4E00)

print(chr(19969))  # 转化成汉字输出
print(chr(98))  # 转化成汉字输出

s3='abc一二三'
print(len(s3))  #字符串的长度

# format ：Hello xxx,today is yyy
print('Hello,%s,today is %s' %('Tom','Sat.'))  # 占位符
print('Hello,%s'  %'Tom')  # 占位符

# $s :字符串 %f:浮点数 %x：16进制数 %d:整数