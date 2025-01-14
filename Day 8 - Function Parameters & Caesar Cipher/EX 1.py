"""
No Of Paint Cans to Cover Wall Area
"""
from math import ceil
def paint_calc(h,w,c):
    area = h * w
    noOfCans = ceil (area / c)
    print(f"You'll need {noOfCans} cans of paint")


height = int(input("Height Of Wall : "))
width = int(input("Width Of Wall : "))
coverage = 5
paint_calc(h=height, w=width, c=coverage)