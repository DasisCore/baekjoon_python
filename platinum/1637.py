# 1637. 날카로운 눈

# 문제
# 동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 원숭이는 좀 특이한 원숭이였다. 어떤 것도 꿰뚫어볼 수 있는 날카로운 눈을 가진 기이한 원숭이였다. 부드러운 눈을 가진 멍멍이는 언제나 날카로운 눈을 가진 원숭이를 부러워했지만 한편으로는 매우 질투했다.
# 어느 날 멍멍이는 원숭이의 날카로운 눈이 너무 샘나서 원숭이를 직접 패고 싶었지만 날카로운 눈으로 찌를까봐 무서워서 때리지는 못하고 대신, 원숭이에게 문제 하나를 던져주었다. 그 문제는 다음과 같다.
# 정수가 여러 개 모여 있는 정수더미가 있다. 그 안에 어떤 특정한 정수 하나만 홀수개 존재하고 나머지 정수는 모두 짝수개 존재한다. 정수더미 속에서 날카로운 눈을 이용해 홀수개 존재하는 정수를 찾아야 하는 문제이다.
# 근데 멍멍이가 문제를 전달해 주려다가 생각해보니 정수더미 안에 정수가 적게 있으면 문제가 너무 쉬워지게 되는 것이다. 그래서 정수더미안에 정수를 무지막지하게 많이 넣기로 했다. 정수더미가 주어졌을 때, 그 안에 홀수개 존재하는 정수를 찾는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 입력의 개수 N이 주어진다. N은 1이상 20,000이하인 수이다. 그 다음 줄부터 N줄에 걸쳐 세 개의 정수 A, C, B가 주어지는데, 이것은 A, A+B, A+2B, ..., A+kB (단, A+kB ≦ C) 의 정수들이 정수더미 안에 있다는 것을 나타낸다. A, B, C는 1보다 크거나 같고 2,147,483,647보다 작거나 같은 정수이다. 정수더미는 N개의 입력이 나타내는 정수들을 모두 포함한다.
#
# 출력
# 첫째 줄에 정수 두 개를 출력하는데, 첫 번째는 홀수개 존재하는 정수를 출력하고, 두 번째는 그 정수가 몇 개 들어있는지 출력한다. 만약 홀수개 존재하는 정수가 없다면 NOTHING을 출력한다.

########################################################################################################

import sys

def check(x):
    global total

    # n줄에 주어진 구간에서 x보다 작거나 같은 수의 개수 구하기
    total = 0
    for i in li:
        # 계산하기 쉽게
        a, b, c = i[0], i[1], i[2]
        check = min(b, x)
        if check < a:
            total += 0
        else:
            total += ((check - a) // c) + 1
    return total

n = int(sys.stdin.readline().strip())
li = []
for i in range(n):
    a, c, b = map(int, sys.stdin.readline().strip().split())
    li.append([a, c, b])

s = 1
e = 2147483649

# 이진 탐색
ans = -1
while s <= e:
    mid = (s + e) // 2

    if check(mid) % 2:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

if ans == -1:
    print("NOTHING")
else:
    print(ans, check(ans) - check(ans - 1))


