import os

FILE_PATH = 'synonym_set.txt'

# 1. create the file first no matter it exists or not
with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write("")

for root, dirs, files in os.walk('.'):
    if('git' not in str(root)):
        for file in files:
            if(file == "output.txt"):
                print(file)
                OUTPUT_PATH = os.path.join(root, file)
                print(OUTPUT_PATH)

                # 2. read the output file in each directory
                with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
                    word_list = f.read().splitlines()
                
                unique_word_list = list(set(word_list)) # make it unique list, and it reorders it.
                # 3. write to the FILE_PATH
                with open(FILE_PATH, 'a', encoding='utf-8') as f:
                    f.write("\n".join(unique_word_list))
                    f.write("\n")
