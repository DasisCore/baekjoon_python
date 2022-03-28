# 16562. 친구비

# 문제
# 19학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다. 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다. 그런 준석이에게도 희망이 있다. 바로 친구비다!
# 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다. 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다. 그래서 준석이는 “친구의 친구는 친구다”를 이용하기로 했다.
# 준석이는 이제 모든 친구에게 돈을 주지 않아도 된다!
# 위와 같은 논리를 사용했을 때, 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구하라.
#
# 입력
# 첫 줄에 학생 수 N (1 ≤ N ≤ 10,000)과 친구관계 수 M (0 ≤ M ≤ 10,000), 가지고 있는 돈 k (1 ≤ k ≤ 10,000,000)가 주어진다.
# 두번째 줄에 N개의 각각의 학생이 원하는 친구비 Ai가 주어진다. (1 ≤ Ai ≤ 10,000, 1 ≤ i ≤ N)
# 다음 M개의 줄에는 숫자 v, w가 주어진다. 이것은 학생 v와 학생 w가 서로 친구라는 뜻이다.
#
# 출력
# 준석이가 모든 학생을 친구로 만들 수 있다면, 친구로 만드는데 드는 최소비용을 출력한다. 만약 친구를 다 사귈 수 없다면, “Oh no”(따옴표 제거)를 출력한다.

##########################################################################################

import sys
# 재귀 제한 늘려주기
sys.setrecursionlimit(1 << 20)

# 일반적인 dfs + 해당 그래프에서 최소비용 찾기
def dfs(cur):
    global cnt

    cnt = min(cnt, li[cur])
    visited[cur] = True
    for i in v[cur]:
        if visited[i]:
            continue
        dfs(i)


n, m, k = map(int, sys.stdin.readline().strip().split())
li = [0] + list(map(int, sys.stdin.readline().strip().split()))

v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    v[a].append(b)
    v[b].append(a)

ans = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    cnt = 10000
    dfs(i)
    ans += cnt

if ans <= k:
    print(ans)
else:
    print("Oh no")
