def sum_of_lists(list_1, list_2):
  list_sum = []
  sum = 0
  for i in range(0, len(list_1)):
    sum = list_1[i] + list_2[i]
    list_sum.append(sum)
  return list_sum

list_1 = []
list_2 = []
print("Enter the numbers for the first list: ")
for i in range(0, 5):
  item = int(input())
  list_1.append(item)

print("Enter the numbers for the second list: ")
for i in range(0, 5):
  item = int(input())
  list_2.append(item)

print(sum_of_lists(list_1, list_2))