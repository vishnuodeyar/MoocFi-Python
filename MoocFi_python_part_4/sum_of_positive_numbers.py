def sum_of_positive_numbers(numbers):
  sum = 0
  for number in numbers:
    if number %2 == 0:
      sum += number
    return sum

mylist = []