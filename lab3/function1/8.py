def has007(nums):
    code = [0,0,7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False
nums = input().split() 
nums = [int(n) for n in nums]  
print(has007(nums))
    