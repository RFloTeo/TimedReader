import random
import time
import keyboard
import sys

files = []
for f in sys.argv[1:]:
    reader = open(f, 'r')
    files.append(reader.read())
    reader.close
files = list(map((lambda w: w[:-1].split("\n")), files))
print('How many seconds between words? ', end='')
delay = float(input())
key = not delay
print('Shuffle the words? (Y/N) ', end='')
shuf = input()
words = [e for l in files for e in l]
if shuf in ['y', 'Y', 'yes', 'Yes']:
    random.shuffle(words)
print('You have', len(words), 'items')
for word in words:
    print(word)
    if key:
        keyboard.wait('Enter')
    else:
        time.sleep(delay)
print('\nDone!')
