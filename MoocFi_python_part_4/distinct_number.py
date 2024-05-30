def distinct_numbers(my_list : list):
  distinct_list = []
  for i in range(0, len(my_list)):
    if my_list[i] not in distinct_list:
      distinct_list.append(my_list[i])
  return distinct_list

def sort_and_distinct_numbers(my_list : list):
  sorted_list = distinct_numbers(my_list)
  sorted_list.sort()
  return sorted_list

my_list = []
for i in range(0,6):
  item = int(input())
  my_list.append(item)

print(distinct_numbers(my_list))
print(sort_and_distinct_numbers(my_list))