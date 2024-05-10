import pandas as pd
import csv
import chinese_converter

converted_list = []
import re

def eliminateSlash(line):
    if '\\' in line:
        line = line.replace('\\', '')
    return line

def tc2sim(line_no_slash):
    global converted_list
    # eliminate the escape character \
    line_no_slash = eliminateSlash(line)

    arr_of_phrases = line_no_slash.split(",")
    for idx, phrase in enumerate(arr_of_phrases):
        m = re.search('[\u4e00-\u9fff]+', phrase)
        if m is not None:
            arr_of_phrases[idx] = chinese_converter.to_simplified(phrase)
        else:
            arr_of_phrases[idx] = phrase
    return ','.join(arr_of_phrases)


df = pd.read_excel("./keyword_Synonym_List_20240331.xlsx")
df = df.fillna('') # fill empty cells with empty string, otherwise when we export to csv, it will be NaN, which is not what we want
df.to_csv(r'./output2.txt', index=None, header=None, sep=',', quoting=csv.QUOTE_NONE, escapechar='\\')

line_list = []
with open("./output2.txt", 'r') as f:
    line_list = f.read().splitlines()

for idx, line in enumerate(line_list):
    line_no_slash = tc2sim(line)
    line_list[idx] = line_no_slash


with open("./output2.txt", 'w') as f:
    f.write("\n".join(line_list))
