a = "S!@#@1FD23154A34"
li = list(a)

for i in range(14,0,-2):
    for j in range(12,0,-4):
        li[j],li[j-4] = li[j-4],li[j]
    li[i-1],li[i-2] = li[i-2],li[i-1]
    
b=''.join(li)
print(b)



这是我的开发分支用于测试111111111111111111111111
