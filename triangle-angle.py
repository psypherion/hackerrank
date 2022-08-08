import math
a = int(input("Enter side A : "))
b = int(input("Enter side B : "))
#h = math.sqrt(a**2 + b**2)
#equal_side = h/2
pi = 22/7
tan_a = a /b
angle_c = math.atan(tan_a)
angle = math.ceil(angle_c *(180/pi) )
print("Angle :  ", angle)
