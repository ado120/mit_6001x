s = 'abcbcd'

long_sub = ''
temp_sub = ''

for i in range(len(s)):
    if s[i] >= s[i-1]:
        temp_sub += s[i]
    else: 
        temp_sub = s[i]
    if len(temp_sub) > len(long_sub):
        long_sub = temp_sub


print('Longest substring in alphabetical order is: ' + long_sub)
print(len(s))