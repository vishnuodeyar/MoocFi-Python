def exercise_points(a):
  if a >= 90:
    return 10
  else:
    points = a // 10
    return points

def total_points(a, b):
  return exercise_points(a) + b

def grade_calculation(a, b):
  points = total_points(a, b)
  if points <= 14:
    return "F"
  elif points <=  17:
    return "1"
  elif points <=  20:
    return "2"
  elif points <= 23:
    return "3"
  elif points <= 27:
    return "4"
  elif points <= 30:
    return "5"
  else:
    return "Out of range"

while(True):
  a = int(input("Enter exercise points: "))
  b = int(input())
  if a == -1:
    break
  else:
    print(grade_calculation(a, b))

print(total_points(99, 15))