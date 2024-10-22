a, b = map(int, input().strip().split(' '))
for i in range(b):
    t=''
    for k in range(a):
        t+='*'
    print(t)