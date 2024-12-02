import random
from collections import Counter


words_list = ['mersedes', 'bmw', 'opel', 'kia', 'optima', 'bugatti', 'lamborghini', 'man', 'woman', 'child']

with open('file.txt', 'w') as file:
    for _ in range(100):
        word = random.choice(words_list) 
        file.write(word + ' ') 

with open('file.txt', 'r') as file:
    content = file.read()


words = content.split()


word_counts = Counter(words)

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
