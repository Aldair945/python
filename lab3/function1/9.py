import math
def volume(radius):
    volume = (4/3) * math.pi * pow(radius,3)
    print(volume)
radius = int(input())
volume(radius)