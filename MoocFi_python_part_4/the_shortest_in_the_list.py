def shortest_in_the_list(my_list : list):
  shortest = " "
  for i in my_list:
    if len(i) < len(shortest):
      shortest = i
  return shortest

print("Enter the words: ")
my_list = []
for i in range(0, 6):
  item = input()
  my_list.append(item)

print(shortest_in_the_list(my_list))