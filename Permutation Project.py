import random

def perm_string(word):
    """
    This function takes a word and returns a random permutation of its 
    letters.
    """
    if not word:
        return ''
    
    # Convert the word to a list of characters, shuffle it, and join back 
    #to a string

help_list = []
for letter in word:
    help_list.append(letter)
random.shuffle(help_list)
help_list = ''.join(help_list)
return help_list

result_list = [] 
product = 1
# This code generates all unique permutations of a given word and prints 
#them along with the total count.

word = input('Enter a word: ').strip().lower()

for letter in word:
    product *= word.index(letter) + 1 
    
while len(result_list) < product:
    
    short_list = perm_string(word)
    
    if short_list not in result_list:
        result_list.append(short_list)

print(f'Number of permutations: {product}')
for word in result_list:
    print(word)