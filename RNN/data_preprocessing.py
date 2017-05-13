# -*- coding: utf-8 -*-
import csv

def tag_function(sentence):     #태그함수
    string=':'      #csv입력시 오류방지
    tag=''
    for i in range(len(sentence)):
        if i == 0:
            string += sentence[i]
            tag+='1 '
        elif sentence[i] != ' ' and sentence[i - 1] == ' ':  # 첫 음절일때
            string += sentence[i]
            tag+='1 '
        elif sentence[i] != ' ' and sentence[i - 1] != ' ':  # 아닐 때
            string += sentence[i]
            tag+='0 '

    return string,tag

def open_csv(num):  #전처리데이터 만들기
    csv_file = open('t'+str(num)+'.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    return csv_writer,0

num=1
csv_writer, cnt = open_csv(num)
text_file = open('answer.txt','r',encoding='utf-8')

for sentence in text_file:
    sentences = sentence.split('.')
    for i in sentences:
        i=i.strip()

        if len(i)>2:         #첫줄, 빈줄 제외
            cnt+=1
            string,tag=tag_function(i)   #태그달기
            csv_writer.writerow([string,tag])   #csv입력

            if cnt==1000000:    #백만기준으로 자르기
                num+=1
                csv_writer, cnt = open_csv(num)

text_file.close()
