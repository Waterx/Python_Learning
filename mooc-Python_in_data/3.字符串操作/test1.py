
s = "I like Python very much 2333 because Python is very cute 666."
num_of_digit = 0
for c in s:
    if c.isdigit():
        num_of_digit = num_of_digit + 1
print("The num of digits:", num_of_digit)

num_of_letters = 0
s_list = s.split(' ')
for letter in s_list:
    if letter.isalpha():
        num_of_letters = num_of_letters + 1

print("The num of letters:", num_of_letters)
s = s.replace('Python', 'Jay', 1)
print(s)


