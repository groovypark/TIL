# 효율성 문제 부족


def solution(words, queries):
    answer = []
    queries_len = set()
    words_len = set()
    for query in queries:
        queries_len.add(len(query))
    for word in words:
        words_len.add(len(word))

    for i in range(len(words)):
        if not len(words[i]) in queries_len:
            del words[i]

    for query in queries:
        count = 0
        idx = []

        if len(query) < min(words_len) or len(query) > max(words_len):
            answer.append(0)
            continue

        for i in range(len(query)):
            if query[i] != '?':
                idx.append(i)

        for word in words:
            equals = True
            if len(word) != len(query):
                continue

            for i in idx:
                if query[i] != '?' and query[i] != word[i]:
                    equals = False
                    break
            if equals:
                count += 1
        answer.append(count)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
# [3, 2, 4, 1, 0]
