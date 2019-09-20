# 가까운 Shop을 찾아라!
# 상점 쿠폰 서비스. User와 제일 가까운 상점부터 보여줌
# User 위치와 상점간의 거리는 100미만일 때, 절삭하고 정렬
# 예) 1174는 1100으로 계산
# 만약 절삭한 거리가 동일하면, 쿠폰이 많은 상점부터 보여줌
# 쿠폰 개수까지 동일하면, 상점의 이름을 숫자, 알파벳 순서(012...AB...YZ)로 보여줌
# User 위치와 상점 정보를 입력하면, 상점을 정렬하여 보여주는 프로그램 작성

# 입력값
# User의 x, y 좌표와 상점 개수
# 상점의 x, y 좌표와 상점의 이름, 쿠폰 개수. 한 줄에 상점 하나씩 (0 <= x <= 9999, 0<= y <= 9999)
    # 상점 이름에 사용되는 글자의 종류는, 숫자와 알파벳 대문자만 사용해서 6자
import math

def main():
    [user_x, user_y, store_num] = [int(x) for x in input().split()]
    stores = {}

    for _ in range(store_num):
        line = input()
        [store_x, store_y, name, coupons] = line.split()
        # 거리 비교
        distance = abs(user_x - int(store_x))**2 + abs(user_y + int(store_y))**2
        distance = (int(math.sqrt(distance)) // 100) * 100
        stores[line] = distance

    s_stores = sorted(stores.items(), key=(lambda x: x[1]))
    for store in s_stores:
        print(store[0])

    return 0

main()


# Input Example
# 7123 4653 4
# 9288 6714 9S7RZV 30
# 6284 8626 CQS1OZ 27
# 6508 4507 Y5J0Q6 12
# 3326 4983 LSPFA8 45

# Output Example
# 6508 4507 Y5J0Q6 12
# 9288 6714 9S7RZV 30
# 3226 4983 LSPFA8 45
# 6284 8626 CQS1OZ 27

# 왜 이렇게 나올까ㅠㅠ
# 6508 4507 Y5J0Q6 12
# 3326 4983 LSPFA8 45
# 9288 6714 9S7RZV 30
# 6284 8626 CQS1OZ 27
