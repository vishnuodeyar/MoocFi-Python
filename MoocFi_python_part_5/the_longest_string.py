def longest_string(string_list: list):
  longest = 0
  longest_string = ""
  for a in string_list:
    if len(a) > longest:
      longest = len(a)
      longest_string = a
  return longest_string

print(longest_string(["a", "ab", "abc", "abcd", "abcde"]))