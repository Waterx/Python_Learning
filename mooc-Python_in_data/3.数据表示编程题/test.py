def countchar(str):
    str = str.lower()
    t = 97   # the ascii no of 'a'
    list = [0 for x in range(26)]
    for i in range(26):
        list[i] = str.count(chr(t))
        t = t + 1
    return list

str = input()
print(countchar(str))
