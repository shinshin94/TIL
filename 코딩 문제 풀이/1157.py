# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳
word = input().upper()
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count #카운트 변수에 입력받은 변수를 카운트 해줌
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1: #중복된 인덱스의 맥스가 2개 이상일때
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))]) #world_list안에서 cnt리스트 안에 가장 갯수많은 인덱스