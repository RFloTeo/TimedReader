import random
import time

print('Enter the words separated by spaces: ', end='')
in_string = input()
print('How many seconds between words? ', end='')
delay = float(input())
print('Shuffle the words? (Y/N) ', end='')
shuf = input()
words = in_string.split(" ")
if shuf in ['y', 'Y', 'yes', 'Yes']:
    random.shuffle(words)
for word in words:
    print(word)
    time.sleep(delay)
print('\nDone!')
