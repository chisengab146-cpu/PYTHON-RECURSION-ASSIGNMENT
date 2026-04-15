word = input("Enter a word: ")

letters = list(word) #array of characters

start = 0
end = len(letters) - 1
palindrome = True

while start < end:
    if letters[start] != letters[end]:
        palindrome = False
        break
    start += 1
    end -= 1

if palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")