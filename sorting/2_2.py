## 성적이 낮은 순서로 학생 출력하기
"""
// problem
모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
// input
첫째 줄 -> 학생 수 N (1 ~ 100,000)
둘째 줄부터 N+1번째 줄까지 학생의 이름과 점수 입력 (이름의 길이와, 성적은 <=100)
// output
모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
"""
# my code
# N 입력 받기
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')
# O(nlogn)
"""
// learn
my code와 동일한 풀이다.
"""