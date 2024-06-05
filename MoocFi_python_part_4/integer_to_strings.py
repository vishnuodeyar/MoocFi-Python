def formatted(my_list):
  new_list = []
  for i in my_list:
    a = f"{i: .2f}"
    new_list.append(a)
  return new_list

print("Enter the numbers: ")
my_list = []
for i in range(0,6):
  item = float(input())
  my_list.append(item)

print(formatted(my_list))