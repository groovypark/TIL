# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가[6, 10, 2]라면[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100, 000 이하입니다.
# numbers의 원소는 0 이상 1, 000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers | return
# [6, 10, 2] | "6210"
# [3, 30, 34, 5, 9] | "9534330"


# 첫 번째 숫자로 정렬
# 두 수를 문자열로 합한 후 크기 비교
def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=lambda x: (x % 10, x))
    sorted_arr = numbers[::-1]

    for n in numbers:
        answer = str(n) + answer

    return answer


numbers = [6, 10, 2]
_return = "6210"
print(solution(numbers) == _return)

numbers = [3, 30, 34, 5, 9]
_return = "9534330"
print(solution(numbers) == _return)


# ---
# 다른 사람 풀이(JS)
# function solution(numbers) {
#     var answer = numbers.map(v=> v + '')
#     .sort((a, b)=> (b+a) * 1 - (a+b) * 1)
#     .join('')

#     return answer[0] == = '0'?'0': answer
# }


# ---
# 다른 사람 풀이
# numbers의 원소는 0 이상 1, 000 이하이기 때문에 x*3
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
