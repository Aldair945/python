def histogram(num):
    for i in num:
        h = '*' * i
        print(h)
num = input().split()
num = [int(n) for n in num]
histogram(num)
    