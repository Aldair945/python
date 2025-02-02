heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
def calc(heads, legs):
    rabbits = (legs - 2 * heads)
    chickens = heads - rabbits
    print(f"Rabbits: {rabbits}")
    print(f"Chickens: {chickens}")
calc(heads, legs)