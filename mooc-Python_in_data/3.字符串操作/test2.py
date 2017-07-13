str = '5'
for i in range(0, 2000-1):
    str = str + '5'
print(str)
print(int(str) % 84)

# 来自网上的方法：
print(int('5'*2000) % 84)
