str = input()

t=''
for i in str:
    if ord(i)>=97:
        t+=chr(ord(i)-32)
    else:
        t+=chr(ord(i)+32)

print(t)