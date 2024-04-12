## for the use of each folder,

- use my_synonym_list if you want to append your list.
- use web_source_synonym_list if you want to run app.py to merge list into big synonym list, result file should be output.txt.
- make your own folder when you want to generate other "output.txt", i.e. another synonym list. Just like 哈工大社会计算与信息检索研究中心同义词词林扩展版 folder.

## this is a script for generating big synonym list for elastic search

1. run python3 app.py in each folder, they will generate "output.txt" in its own folder.
2. run python3 app.py in parent folder, it will grep the "output.txt" from each folder and merge them into "synonym_set.txt"

### the result file you want:

synonym_set.txt

### the reason I decouple this codebase, simply because it's easier to debug and manage.
