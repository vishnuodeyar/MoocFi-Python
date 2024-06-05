def all_the_longest_in_the_list(my_list : list):
  longest = " "
  new_list = []
  for i in my_list:
    if len(i) > len(longest):
      longest = i
  for i in my_list:
    if len(i) == len(longest):
      new_list.append(i)
  return new_list

print("Enter the words: ")
my_list = []
for i in range(0,6):
  item = input()
  my_list.append(item)
print(all_the_longest_in_the_list(my_list))