def has33(num):
    for i in range(len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False
num = input().split() 
num = [int(n) for n in num]  
print(has33(num))