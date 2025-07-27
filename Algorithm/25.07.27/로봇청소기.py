from collections import deque


current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 1. 루트 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
# 4. 2부터 반복한다.
# 5. 큐가 비면 탐색을 종료한다.

# 왼쪽으로 회전
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4
# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map) # 행의 개수
    m = len(room_map[0]) # 열의 개수

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    counts_of_departments_cleaned = 1 # 청소한 칸의 개수
    room_map[r][c] = 2
    queue = deque([[r, c, d]]) # 위치와 방향정보 저장, 1번완료
    # 큐에는 어느 한 값만 넣는게 아니라 우리가 알아야 할 여러 정보를 넣어도 된다.

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        # 네 방향 모두 탐색
        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d) # 북 서
            new_r, new_c = r + dr[temp_d], c + dc[temp_d] # 위 방향으로 간 이후의 새로운 위치

            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                # 청소가 안되어 있다면
                room_map[new_r][new_c] = 2 # 구분을 위한 임의의 값
                counts_of_departments_cleaned += 1
                # 청소를 했으면 다시 반복
                queue.append([new_r, new_c, temp_d])
                break # 해당 지역에서 또 도는걸 그만 해야하니깐

            # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            elif i == 3: # 빠져나가지 못하고 다시 북쪽으로 돌아왔을 때. 즉 이미 모두 청소가 되어있거나 벽인 경우
                back_d = get_d_index_when_go_back(d)
                new_r, new_c = r + dr[back_d], c + dc[back_d]
                # 다시 반복
                queue.append([new_r, new_c, d])
                # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘
                if room_map[new_r][new_c] == 1: # 새로운 위치가(후진한 위치) 벽이라면 끝
                    return counts_of_departments_cleaned
    return

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
