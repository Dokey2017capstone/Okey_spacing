# -*- coding: utf-8 -*-

from __future__ import unicode_literals     #unicode 문제 해결
from io import open             #encoding='utf-8'을 하기 위해서
import pycrfsuite                           #crf


def feature_function(sentence):        #특징함수
    feature_string=[]       # [[나,3:는],[는,2:나,3:먹],[먹,1:나,2:는,3:다],[는,1:는,2:먹,3:다],[다,1:먹,2:는]]

    for i in range(len(sentence)):
        syllable_feature = []  # [먹,1:나,2:는,3:다]
        syllable_feature.append(sentence[i])

        if i > 1:
            syllable_feature.append('1:' + sentence[i - 2])
        if i > 0:
            syllable_feature.append('2:' + sentence[i - 1])
        if i < len(sentence) - 1:
            syllable_feature.append('3:' + sentence[i + 1])

        feature_string.append(syllable_feature)
    return feature_string


def result_function(sentence, tag):     #출력스트링
    result = ''
    for i in range(len(sentence)):
        if tag[i] == '1':
            result += (' ' + sentence[i])
        else:
            result += sentence[i]

    if result[0] == ' ':  # 결과의 처음이 띄어져있을 때
        result = result[1:]
    return result


def accuracy_function(result_list):     #정확도
    index = -1
    cnt = 0

    answer_file = open('answer.txt', 'r', encoding='utf-8')
    for sentence in answer_file:
        if index == -1:
            pass
        else:
            if sentence.strip() == result_list[index]:
                cnt += 1
        index += 1
    answer_file.close()

    accuracy = (cnt / float(index)) * 100
    return accuracy


test_file = open('test.txt','r',encoding='utf-8')         #파일 전체 읽기
result_file = open('result.txt','w',encoding='utf-8')

crf_tagger = pycrfsuite.Tagger()  # Taggger 클래스는 crf모델을 사용하여 입력 시퀀스의 레이블 시퀀스를 예측하는 기능을 제공한다.
crf_tagger.open('crf.crfsuite')  # 모델 파일을 연다

result_list=[]
first_flag = False
for sentence in test_file:

    sentence = sentence.strip()

    feature_string = feature_function(sentence)     #특징함수적용
    tag = crf_tagger.tag(feature_string)    # 훈련된 모델의 항목 순서에 대한 레이블 순서를 예측
    result = result_function(sentence, tag)     #결과도출

    if first_flag:
        result_file.write(result + '\n')
        result_list.append(result)
    first_flag=True

#정답과 비교
print 'accuracy :',accuracy_function(result_list)

crf_tagger.close()  # 모델 닫기
test_file.close()
result_file.close()
#answer_file은 첫줄공백