def count_matching_elements(my_matirx: list, element: int):
  b = 0
  for a in my_matirx:
      for c in a:
          if c == element:
              b += 1
  return b

matrix = [[12,3,4], [34,56,3], [3,34,3]]
print(count_matching_elements(matrix, 12))