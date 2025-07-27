seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2
}

# n번째 티켓을 가진 사람이 앉을 수 있는 방법?
# 1. n번째 좌석에 앉거나
# -> 좌석은 n-1개가 남아있고, 사람도 n-1 번째 티켓까지 가진 사람이 있는 상황.
# => n-1명의 사람들을 좌석에 배치하는 방법

# 2. n-1 번째 좌석에 앉거나
# n-1번째 티켓을 가진 사람은 n 번째 좌석에 앉아야만 한다.
# -> 좌석은 n-2개가 남아있고, 사람도 n-2번째 티켓까지 가진 사람이 있는 상황.
# => n-2명의 사람들을 좌석에 배치하는 방법

# F(n): n명의 사람들을 좌석에 배치하는 방법
# F(n) = F(n-1) + F(n-2)
def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1


    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
