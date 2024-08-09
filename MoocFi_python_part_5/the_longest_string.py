def longest_string(string_list: list):
  longest = 0
  longest_string = ""
  for a in string_list:
    if len(a) > longest:
      longest = len(a)
      longest_string = a
  return longest_string

print("Enter the list: ")
my_list = []
for i in range(0,6):
  item = input()
  my_list.append(item)

print(longest_string(my_list))
