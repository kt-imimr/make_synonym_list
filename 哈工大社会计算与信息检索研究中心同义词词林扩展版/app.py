import re

FILE_PATH = '哈工大社会计算与信息检索研究中心同义词词林扩展版.txt'

new_word_list = []

def main():
    try:
        with open(FILE_PATH, 'r', encoding='gb18030') as f:
            word_list = f.read().splitlines()
    except UnicodeDecodeError as e:
        print("error")

    for group in word_list:
        words = re.split(r'[@=#]', group)[1].strip().split(" ")
        if(len(words) == 1): continue
        words_str = ", ".join(words)
        print("🐍 File: 哈工大社会计算与信息检索研究中心同义词词林扩展版/app.py | Line: 22 | main ~ words_str",words_str)
        new_word_list.append(words_str)

    unique_word_list = list(set(new_word_list)) # make it unique list, and it reorders it.
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_word_list))

main()