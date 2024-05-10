import os

word_list= []
with open("./my_synonym_list/output2.txt", 'r', encoding='utf-8') as f:
    word_list = f.read().splitlines()

with open("synonym_set.txt", 'a', encoding='utf-8') as f:
    f.write("\n")
    f.write("\n".join(word_list))
    f.write("\n")



