import random
from collections import Counter


words_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'pineapple', 'pear', 'peach', 'cherry']

with open('example.txt', 'w') as file:
    for _ in range(100):
        word = random.choice(words_list) 
        file.write(word + ' ') 

with open('example.txt', 'r') as file:
    content = file.read()


words = content.split()


word_counts = Counter(words)

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
