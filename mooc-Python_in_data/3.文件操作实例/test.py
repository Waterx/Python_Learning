text = '''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind'''

with open('Blowing in the wind.txt', 'w') as f:
    f.write(text)

with open('Blowing in the wind.txt', 'r+') as f:
    text = f.readlines()

text.insert(0, "Blowin' in the wind")
text.insert(1, "Bob Dylan")
text.append('1962 by Warner Bros. Inc.')

with open('Blowing in the wind.txt', 'w') as f:
    for i in enumerate(text):
        f.write(i)
