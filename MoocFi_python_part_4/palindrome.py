def palindrome(a):
  return a == a[::-1]

string = input("Check if the word is a palindrome: ")
print(palindrome(string))