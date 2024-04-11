import re


def extractor():
    try:
        with open('哈工大社会计算与信息检索研究中心同义词词林扩展版.txt', 'r', encoding='gb18030') as f:
            word_list = f.read().splitlines()
    except UnicodeDecodeError as e:
        # print(f"🐍 File: 哈工大社会计算与信息检索研究中心同义词词林扩展版/app.py | Line: 8 | extractor ~ error", e)
        # with open('哈工大社会计算与信息检索研究中心同义词词林扩展版.txt', 'rb') as f:
        #     word_list = f.read().decode('gb18030').splitlines()
        #     print("🐍 File: 哈工大社会计算与信息检索研究中心同义词词林扩展版/app.py | Line: 11 | extractor ~ word_list", word_list)
        print("error")

    # remove duplicate words from the list
    # set() will only keep unique elements, then we convert it back to a list
    # word_list = list(set(word_list))
    
    for group in word_list:
        words = re.split(r'[@=#]', group)[1].strip().split(" ")
        words_str = ",".join(words)
        print("🐍 File: 哈工大社会计算与信息检索研究中心同义词词林扩展版/app.py | Line: 22 | extractor ~ words_str",words_str)

    with open("words.txt", "w", encoding="utf-8") as f:
        f.write(words_str)
extractor()