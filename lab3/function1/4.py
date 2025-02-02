def filter_prime(numbers):
    prime = []
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break  
        else:
            prime.append(num)  
    return prime

numbers = input().split()
numbers = [int(num) for num in numbers]
print(filter_prime(numbers))