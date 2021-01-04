## 숫자 카드 게임

# my code
n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
min_arr=[]
for i in range(n):
  min_arr.append(min(data[i]))
print(max(min_arr))
# O(n2)