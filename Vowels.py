mytext = 'beautiful!'
vowels = ['a', 'e', 'i', 'o', 'u']
result = ''
for letter in mytext:
    if letter not in vowels:
        result += letter

print(result)
