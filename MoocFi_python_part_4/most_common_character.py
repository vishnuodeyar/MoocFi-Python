def most_common_character(string: str):
  count = string[0]
  for i in string:
    if string.count(i) > string.count(count):
      count = i
  return count


a = input("Enter the words: ")
print(most_common_character(a))