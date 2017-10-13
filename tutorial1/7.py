s = 'This is the brown fox that jumps over the black dog'
word_list = s.split()
word_dict = {}
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1
print(word_dict)
