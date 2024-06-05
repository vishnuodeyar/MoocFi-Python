def everthing_reversed(reverse: list):
  new_list = []
  for i in reverse:
    new_list.append(i[::-1])
  return new_list

print("Enter the words: ")
my_list = []
for i in range(0,6):
  item = input()
  my_list.append(item)
print(everthing_reversed(my_list))