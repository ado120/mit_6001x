s = 'azcbobobegghakl'
word = 'bob'

count = 0
len_word = len(word)

for i in range(len(s)):
    if s[i:i+len(word)] == word:
        count += 1

print('Number of times bob occurs is: ' + count)

    