# 문제 설명

# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10, 000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 입출력 예
# genres | plays | return
# [classic, pop, classic, classic, pop] | [500, 600, 150, 800, 2500] | [4, 1, 3, 0]

# 입출력 예 설명
# classic 장르는 1, 450회 재생되었으며, classic 노래는 다음과 같습니다.

# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3, 100회 재생되었으며, pop 노래는 다음과 같습니다.

# 고유 번호 4: 2, 500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의[4, 1]번 노래를 먼저, classic 장르의[3, 0]번 노래를 그다음에 수록합니다.
# ---


def solution(genres, plays):
    answer = []
    genre_types = set(genres)
    
    # 인기 장르 순서

    best_play = max(plays)

    # while genre_types:
    #     if answer % 2 == 0:
    #         genre_types.remove(current_genre)
    #         best_play = max(plays)
    #         best_idx = plays.index(best_play)
    #         current_genre = genres[best_idx]
    #         answer.append(best_idx)
    #         best_play = 0
    #         play[best_idx] = -1
    #         continue

    #     for num in enumerate(plays, idx):
    #         if genres[idx] == current_genre:
    #             best_play = max(best_play, num)

    #     best_idx = plays.index(best_play)
    #     answer.append(best_idx)

    #     best_play = 0
    #     play[best_idx] = -1

    return best_idx


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# print(solution(genres, plays))  # [4, 1, 3, 0]

# ---
# 다른 사람 풀이

def solution2(genres, plays):
    '''
    각 노래의 grouping을 진행할 변수를 선언해준다.
    다음과 같은 구조를 가지게 된다.
    {
        '장르이름': {
            't': 전체 재생 시간
            'l': [노래정보리스트, {'v': 재생시간, 'i': 고유번호}]
        }
    }
    '''
    d = {}
    # 노래 갯수 만큼 loop를 돌며 grouping을 진행한다.
    for i in range(len(genres)):
        # 장르에 해당하는 key가 없으면 새로 만들어준다.
        if not genres[i] in d:
            d[genres[i]] = {'t': 0, 'l': []}
        d[genres[i]]['l'].append({'v': plays[i], 'i': i})
        d[genres[i]]['t'] += plays[i]

    # 정렬을 위해 list 형태로 바꿔준다.
    # 앞으로의 연산이나, answer에는 장르 이름이 필요없기에 문제없다.
    d = list(d.values())
    d = sorted(d, key=lambda k: k['t'], reverse=True)
    answer = []
    # 각 장르별 재생 횟수를 정렬하고, answer를 구한다.
    for i in range(len(d)):
        v = d[i]['l']
        v = sorted(v, key=lambda k: k['v'], reverse=True)
        for j in range(2 if len(v) >= 2 else len(v)):
            answer.append(v[j]['i'])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution2(genres, plays))  # [4, 1, 3, 0]

# ---
# 다른 사람 풀이2

def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer
