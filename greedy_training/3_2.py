## 문자열 뒤집기
"""
// problem
0과 1로만 이루어진 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집어서
문자열에 있는 모든 숫자를 전부 같게 만든다.
// input
첫 째줄 -> 0과 1로만 이루어진 문자열 S (len(S) <=1000000)
// output
뒤집기 최소 횟수
"""
# study
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
# O(n)
"""
// learn
my code와 동일한 풀이다.
다만, 여기서는 data[i]와 data[i+1] 값을 비교해가며 뒤집기를 체크한다.
"""