def unique_list(list):
    unique = []
    for i in list:
        if i not in unique and list.count(i) == 1:
            unique.append(i)
    print(unique)
list = input().split()
list = [int(n) for n in list]
unique_list(list)