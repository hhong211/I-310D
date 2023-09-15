import math

def calculate_volume_of_sphere(radius):
  v = (4/3) * math.pi * (radius ** 3)
  return v

radius1 = 30
v1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {v1}")

radius2 = 40
v2 = calculate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius1} is: {v2}")
