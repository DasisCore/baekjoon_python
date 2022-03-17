# 14244. 트리 만들기

# 문제
# n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.
# 항상 정답이 존재하는 경우만 입력으로 주어진다.
# 트리는 사이클이 없는 연결 그래프이고, 리프는 차수가 1인 노드를 의미한다.
#
# 입력
# 첫째 줄에 n과 m이 주어진다. (3 ≤ n ≤ 50, 2 ≤ m ≤ n-1)
#
# 출력
# 첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다. 트리의 정점은 0번부터 n-1번까지 이다.

########################################################################################

n, m = map(int, input().split())

if m == 2:
    for i in range(n - 1):
        print(i, i + 1)

else: # m이 3 이상
    print("0 1")
    for i in range(2, m + 1):
        print(1, i)
    for j in range(m, n - 1):
        print(j, j + 1)



n, m = map(int, input().split())

# 리프의 개수
leaf = 0
if m == 2:
    leaf = 1  # 중심 노드를 리프로 포함

last_leaf = 0
for i in range(1, n):
    if m > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i