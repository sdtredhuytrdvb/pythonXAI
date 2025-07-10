import random

a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)

i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break
    i += 1

for i in range(5):
    print(i)
    if i == 3:
        break

print(random.randrange(7))
print(random.randrange(1, 7))
print(random.randrange(1, 7, 2))
print(random.randint(1, 6))
ans = random.randint(1, 100)
while True:
    num = int(input(f"請輸入一個1~100的整字："))
    if num < 0 or num > 100:
        print("請輸1~100的整數")
    elif num > ans:
        print("太大了")
    elif num < ans:
        print("太小了")
    else:
        print("答對了")
        break
