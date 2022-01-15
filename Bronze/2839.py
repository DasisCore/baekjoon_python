# 2839. 설탕 배달

# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다.
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때,
# 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력 :
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


sugar = int(input())

f_kg = sugar//5 #최대로 들 수 있는 5kg 봉지 수
t_kg = sugar//3 #최대로 들 수 있는 3kg 봉지 수

answer = []
for i in range(0, f_kg+1): #5kg봉지 0개부터 최대 수
    five = i
    for j in range(0, t_kg+1): #3kg봉지 0개부터 최대 수
        if 5*i + 3*j == sugar: #N에 맞으면 리스트에 추가
            con = i+j
            answer.append(con)

if len(answer) != 0: # answer에 값이 없으면 -1 출력
    print(min(answer))
else:
    print(-1)