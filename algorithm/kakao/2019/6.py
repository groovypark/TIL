# 못풀겠따
def solution(n, weak, dist):
    if max(dist) == n:
        return 1

    answer = -1
    dist = dist[::-1]
    weak_dist = []
    for i in range(len(weak)-1):
        weak_dist.append(weak[i+1] - weak[i])
    weak_dist.append(n-weak[-1] + weak[0])

    # 가장먼길이
    max_dist = max(weak_dist)
    max_idx = []
    for i in range(len(weak_dist)):
        if weak_dist[i] == max_dist:
            max_idx.append(i)

    # 가장먼길이부터 시계방향
    for friend in dist:
        for max_i in max_idx:
            distance = weak_dist[::]
            cur = 0
            i = max_i + 1
            while friend > cur and i != max_i and i < len(distance):
                cur += distance[i]
                distance[i] = 0
                distance[i-1] = 0
                i += 1
        print(distance)
        if 0 in distance and sum(distance) != 0:
            answer += 1

    # 가장먼길이부터 반시계방향

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
