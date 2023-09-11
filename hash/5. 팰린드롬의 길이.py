"""
문자열이 주어지면 해당 문자열의 문자들을 가지고 만들 수 있는 최대길이 팰린드롬을 만들고
그 길이를 구하세요. 문자열은 소문자로만 이루어져 있습니다.
만약 "abcbbbccaaeee" 가 주어진다면 만들 수 있는 가장 긴 팰린드롬은 "ebbcaaacbbe"이고
답은 11입니다.
"""
from collections import Counter


def solution(s: str) -> int:
    str_hash = Counter(s)
    odd = 0
    for key in str_hash:
        if str_hash[key] % 2 != 0:
            odd += 1

    return len(s) - odd + 1 if odd > 0 else len(s)


print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
