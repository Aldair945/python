class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def checking(self, number):
        if number < 2:
            return False
        if number == 2:  # 2 is the only even prime number
            return True
        if number % 2 == 0:  # Exclude other even numbers
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    def filtering(self):
        return list(filter(lambda x: self.checking(x), self.numbers))

numbers = list(map(int, input("Enter numbers: ").split()))
prime_get = Prime(numbers)
print(f"Prime numbers are: {prime_get.filtering()}")
