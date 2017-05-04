# -*- coding: utf-8 -*-
import csv

def tag_function(sentence):     #태그함수
    string=':'      #csv입력시 오류방지
    tag=''
    for i in range(len(sentence)):
        if i == 0:
            string += sentence[i]
            tag+='1 '
        elif i == (len(sentence) - 1):  # 맨 뒤 unicode인식
            pass
        elif sentence[i] != ' ' and sentence[i - 1] == ' ':  # 첫 음절일때
            string += sentence[i]
            tag+='1 '
        elif sentence[i] != ' ' and sentence[i - 1] != ' ':  # 아닐 때
            string += sentence[i]
            tag+='0 '

    return string,tag


text_file = open('raw_data.txt','r',encoding='utf-8')
csv_file = open('training.csv','w',newline='')
csv_writer = csv.writer(csv_file)

for sentence in text_file:
    if len(sentence)>2:         #첫줄, 빈줄 제외
        sentence.strip()
        string,tag=tag_function(sentence)   #태그달기
        csv_writer.writerow([string,tag])   #csv입력

text_file.close()
csv_file.close()