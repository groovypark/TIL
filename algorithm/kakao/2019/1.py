def solution(s):
    answer = len(s)
    for l in range(1, (len(s)+1)//2+1):
        cut = ""
        num = 0
        total = 0
        rear = 0
        for i in range(0, len(s), l):
            if i+l <= len(s):
                now = s[i: i+l]
                if cut == now:
                    num += 1
                    continue
                if cut == "":
                    cut = now
                    num = 1
                    continue
                cut = now
                total += l
                if num > 1:
                    if num < 10:
                        total += 1
                    elif num < 100:
                        total += 2
                    else:
                        total += 3
                num = 1
            else:
                total += l
                if num > 1:
                    if num < 10:
                        total += 1
                    elif num < 100:
                        total += 2
                    else:
                        total += 3
                num = 0
                rear = len(s) - i
            if total > answer:
                break
        if num != 0:
            total += l
            if num > 1:
                if (num < 10):
                    total += 1
                elif num < 100:
                    total += 2
                else:
                    total += 3
        answer = min(total+rear, answer)

    return answer


print(solution("abcabcdede"))
