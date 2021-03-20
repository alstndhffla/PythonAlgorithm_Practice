from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAS', 'FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')

"""
튜플 t 에는 int 형 정수와 float 형 실수인 원소가 섞여 있지만 검색하는데 문제가 없다.
str 형 문자열 s 안에서는 문자를 검색할 수도 있다(문자열도 시퀀스이기 때문)
a는 문자열의 배열(모든 원소가 str형이고 list 형인 리스트)인데, 검색을 정확하게 수행한다.
"""
