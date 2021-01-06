## 왕실의 나이트
"""
// problem
8*8 좌표 평면상에서 [(1~8) * (a~h)] 현재 나이트가 위치한 좌표로부터 이동할 수 있는 경우의 수를 구한다.
나이트는 실제 체스 나이트의 움직임과 같다.
// input
현재 나이트가 위치한 좌표 (ex. a1)
// output
나이트가 이동할 수 잇는 경우의 수
"""
# study
data=list(input())
x=int(data[1])
y=ord(data[0])-ord('a')+1
steps=[(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
result=0
for step in steps:
  nx=x+step[0]
  ny=y+step[1]
  if 1<=nx<=8 and 1<=ny<=8:
    result+=1
print(result)
# O(1)
"""
// learn
기존 dx, dy 두 리스트를 사용하는 것 대신 튜플로 구성된 리스트를 사용할 수 있다.
"""