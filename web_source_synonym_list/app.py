import re
import os 

FOLDER_PATH = '.'

FILE_PATH = 'output.txt'

new_word_list = []

# 1. create the file first no matter it exists or not
with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write("")

for root, dirs, files in os.walk('.'):
    try:
        for file in files:
            if('output.txt' not in files or 'py' not in files):
                source_path = file

                # 2. read the source_path
                with open(source_path, 'r') as f:
                    word_list = f.read().splitlines()
                    for line in word_list:
                        if('Copyright' in line):
                            word_list.remove(line)

                # 3. append to the FILE_PATH
                with open(FILE_PATH, 'a') as f:
                    f.write("\n".join(word_list))
    except:
       print("error")
