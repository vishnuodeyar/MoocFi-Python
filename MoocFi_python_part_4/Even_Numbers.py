def even_numbers(my_list : list):
  new_list = []
  for i in my_list:
    print(i)
    if i % 2 == 0:
      new_list.append(i)
  return new_list

my_list = []
for i in range(0,6):
  item = int(input())
  my_list.append(item)
print(my_list)

print(even_numbers(my_list))