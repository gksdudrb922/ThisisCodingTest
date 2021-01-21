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
n=int(input())
data=[]
for _ in range(n):
  name,score=input().split()
  data.append((name,int(score)))

def less_score(data):
  return data[1]
result=sorted(data,key=less_score)
for info in result:
  print(info[0],end=' ')
# O(nlogn)