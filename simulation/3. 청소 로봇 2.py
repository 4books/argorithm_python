"""
청소 로봇은 다음 규칙에 따라 이동합니다.
1. 'U' 명령은 로봇이 위쪽으로 한 칸 이동합니다.
2. 'R' 명령은 로봇이 오른쪽으로 한 칸 이동합니다.
3. 'L' 명령은 로봇이 왼쪽으로 한 칸 이동합니다.
4. 'D' 명령은 로봇이 아래쪽으로 한 칸 이동합니다.
5. 만약 로봇이 명령을 수행할 경우 격자판 밖으로 나가는 경우라면 로봇은 해당 명령을 수행
하지 않고 무시합니다.
매개변수 n에 격자판 크기가 주어지고, moves에 청소 로봇에 명령을 내린 문자들이 차례대로
나열된 명령 문자열이 주어지면 청소 로봇이 최종적으로 멈춘 위치를 반환하는 프로그램을 작
성하세요.
"""


def solution(n, moves):
    x = y = 0

    return [x, y]


print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))
