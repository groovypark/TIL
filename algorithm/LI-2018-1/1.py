# 문자열 압축하기
# 시간 복잡도 표시
# RLE(Run Length Encoding) : 문자열을 나타난 횟수만큼 표시하여 인코딩 하는 기법
# 예) AAAAAADDC -> 6A2D1C
# RLE를 구현하는 프로그램을 작성
# 입력 
# 1 <= T <= 100
# 1 <= 단어길이 <= 200 (단어 중간 공백 없고, 알파벳 대문자만 사용)

def main():
    T = int(input())
    for i in range(T):
        word = input()
        alph = word[0]
        answer = ''
        count = 0
        for i in range(len(word)+1):
            if alph == word[i-1] and i == len(word):
                answer += str(count) + alph
                break
            if alph != word[i]:
                answer += str(count) + alph
                alph = word[i]
                count = 1
                continue
            count += 1
        print(answer)
    return 0

main()

# test
# 2
# AAAAAADDC -> 6A2D1C
# WWWWWBWWWWBBWWWWWWBBBWWWWW -> 5W1B4W2B6W3B5W
