word = input("Enter a word: ")

is_palindrome = True

for i in range(len(word)):
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")