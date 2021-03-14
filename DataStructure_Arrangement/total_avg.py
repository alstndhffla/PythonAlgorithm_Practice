# 시험성적 5개를 입력받아 합계와 평균을 구하기

s1 = int(input('시험성적을 입력하세요:'))
s2 = int(input('시험성적을 입력하세요:'))
s3 = int(input('시험성적을 입력하세요:'))
s4 = int(input('시험성적을 입력하세요:'))
s5 = int(input('시험성적을 입력하세요:'))

total = 0
total += s1
total += s2
total += s3
total += s4
total += s5

print(f'합계는 {total}, 평균은 {total/5}')