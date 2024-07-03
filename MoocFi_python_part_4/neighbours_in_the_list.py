def longest_series_in_neighbours(my_list : list):
  longest = 1
  result = 1
  for i in range(1, len(my_list)):
    if abs(my_list[i] - my_list[i-1]) == 1:
      result += 1
    else:
      result = 1
    longest = max(longest, result)
  return longest

mylist = [2, 22, 3, 4, 5, 99, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(longest_series_in_neighbours(mylist))