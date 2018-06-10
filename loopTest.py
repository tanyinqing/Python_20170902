
list1=['a','c','b','d',]
tuple1=(1,3,2,4)
for i in list1:
    print(i)
for j in tuple1:
    print(j)
list2=[1,2,-3,4,555,6,789,8,9,10]
sum=0
for k in list2:
    sum +=k
print(sum)
sum=3
while sum>0:
    print('test...')
    sum-=1
n = 1
# break continue
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1
# print 100 之内的所有奇数
while n < 100:
    n = n + 1  # Java n++;
    if n % 2 == 0:  # n 是偶数
        continue
    print(n)
