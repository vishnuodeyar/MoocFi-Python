def no_vowels(a):
  vowels = ['a,', 'e', 'i', 'o', 'u']
  for i in a:
    if i in vowels:
      a = a.replace(i, '')
  return a

a = input("Enter the words: ")
print(no_vowels(a))