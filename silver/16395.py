# 16395. 파스칼의 삼각형

# 문제
# 파스칼의 삼각형은 이항계수를 삼각형 형태로 배열한 것인데, 블레즈 파스칼(1623-1662)을 따라 이름 붙여졌다.
# 단순한 형태로, 파스칼의 삼각형은 다음과 같은 방법으로 만들 수 있다.
# N번째 행에는 N개의 수가 있다.
# 첫 번째 행은 1이다.
# 두 번째 행부터, 각 행의 양 끝의 값은 1이고, 나머지 수의 값은 바로 위 행의 인접한 두 수의 합이다.
# 예를 들어, n=3이면 3번째 행의 2번째 수는 위 행의 인접한 두 수 (1과 1)을 더해서 만든다.
# n=6일 때, 파스칼 삼각형의 6번째 행의 10은 5번째 행의 인접한 두 수(4와 6)을 더해서 구한다.
# 같은 방식으로 n=11일 때, 다음과 같은 파스칼의 삼각형을 만들 수 있다.
# 정수 n과 k가 주어졌을 때 파스칼의 삼각형에 있는 n번째 행에서 k번째 수를 출력하는 프로그램을 작성하시오.  이때, 이 수는 이항계수 C(n-1,k-1)임에 주의하시오.
#
# 입력
# 첫째 줄에 정수 n과 k가 빈칸을 사이에 두고 차례로 주어진다. 이 때, 1 ≤ k ≤ n ≤ 30을 만족한다.
#
# 출력
# 첫째 줄에 n번째 행에 있는 k번째 수를 출력한다.

###################################################################################################################

n, k = map(int, input().split())

li = [0, 1, 0] # 0으로 패딩을 한 1열
i = 1
while i != n: # 해당 행에 도착할 때까지
    temp = []
    for i in range(len(li) - 1): # li가 3개이면 2번만 계산
        temp.append(li[i] + li[i + 1])
    temp = [0] + temp + [0] # 계산의 편의를 위해 양옆에 패딩
    li = temp
    i += 1
print(li[k]) # 해당 열의 k번째 인덱스