"""
소문자로만 이루어진 문자열이 주어지면 해당 문자열의 문자들의 순서를 재배치해서 팰린드롬
(회문)을 만들 수 있는지를 확인하고 싶습니다. 만약 "abbac"같은 문자열은 문자들을 "abcba"
로 재 배치하면 팰린드롬을 만들 수 있습니다.
매개변수 s에 문자열이 주어지면 해당 문자열이 재 배치를 통해 팰린드롬을 만들 수 있으면
True를 못 만들면 False를 반환하는 프로그램을 작성하세요.
"""

from collections import Counter


def solution(s: str) -> bool:
    answer = False
    str_hash = Counter(s)
    odd = 0
    for key in str_hash:
        if str_hash[key] % 2 != 0:  # 홀수
            odd += 1
            if odd > 1:
                return False

    return True


print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
