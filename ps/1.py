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
# my code
pos=input()
x=int(pos[1])
y=ord(pos[0])-96
dx=[-2,-2,-1,1,2,2,-1,1]
dy=[-1,1,2,2,1,-1,-2,-2]
result=0
for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]
  if 0<nx<=8 and 0<ny<=8:
    result+=1
print(result)
# O(1)