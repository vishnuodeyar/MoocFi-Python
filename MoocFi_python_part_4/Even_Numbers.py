def sum_of_positive_numbers(my_list):
  sum = 0
  for i in my_list:
    sum += i
  return sum

my_list = []
n = int(input("Enter the size of the list: "))


print("\n")

for i in range(0, n):
  print(f"Enter the number at index {i}")
  item = int(input())
  my_list.append(item)

print(sum_of_positive_numbers(my_list))

