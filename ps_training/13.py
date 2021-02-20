## 치킨 배달
"""
// problem
이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다.
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며,
각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
// input
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
// output
치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
"""
# my code
from itertools import combinations
def city_distance(house,chicken):
  chicken_distance=0
  for housePoint in house:
    distance=50
    r1=housePoint[0]
    c1=housePoint[1]
    for chickenPoint in chicken:
      r2=chickenPoint[0]
      c2=chickenPoint[1]
      distance=min(distance,abs(r1-r2)+abs(c1-c2))
    chicken_distance+=distance
  return chicken_distance

n,m=map(int,input().split())
house=[]
chickens=[]
for i in range(n):
  data=list(map(int,input().split()))
  for j in range(n):
    if data[j]==1:
      house.append((i+1,j+1))
    elif data[j]==2:
      chickens.append((i+1,j+1))
chicken_combi=list(combinations(chickens,m))
result=2500
for chicken in chicken_combi:
  result=min(result,city_distance(house,chicken))
print(result)
# O(n3)

#new
from itertools import combinations
n,m=map(int,input().split())
city=[]
houses=[]
chicken_home=[]
for i in range(n):
  city.append(list(map(int,input().split())))
  for j in range(n):
    if city[i][j]==1:
      houses.append((i,j))
    elif city[i][j]==2:
      chicken_home.append((i,j))


chicken_combinations=list(combinations(chicken_home,m))
result=1e9
for chickens in chicken_combinations:
  city_chicken_distance=0
  for house in houses:
    chicken_distance=100
    for chicken in chickens:
      chicken_distance=min(chicken_distance,abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
    city_chicken_distance+=chicken_distance
  result=min(result,city_chicken_distance)
print(result)