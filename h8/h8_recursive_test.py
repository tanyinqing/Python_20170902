
# n!=n*(n-1)*...*1  recursive递归函数
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(9))
print(fact(100))
'''
多行注释 # A B C n
'''
def hanoi(src,use,dest,n):
    if n==1:
        print(src,'->',dest)
    else:
        hanoi(src,dest,use,n-1)
        print(src,'->',dest)
        hanoi(use,src,dest,n-1)
hanoi("A","B","C",3)