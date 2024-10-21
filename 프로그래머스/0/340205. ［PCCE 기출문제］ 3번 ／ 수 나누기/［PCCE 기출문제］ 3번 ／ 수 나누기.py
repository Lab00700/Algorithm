number = int(input())

answer = 0

for i in range(len(list(str(int(number/1))))):
    answer += number % 100
    number //= 100

print(answer)