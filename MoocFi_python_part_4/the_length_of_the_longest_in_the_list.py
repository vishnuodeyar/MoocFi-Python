def the_length_of_the_longest_in_the_list(my_list : list):
  longest = ""
  for i in my_list:
    if len(i) > len(longest):
      longest = i
  return longest, len(longest)

print("Enter the names: ")
my_list = []
for i in range(0,6):
  item = input()
  my_list.append(item)

print(the_length_of_the_longest_in_the_list(my_list))