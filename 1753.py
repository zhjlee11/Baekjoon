import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

graph = {}

# 입력
V, E = map(int, input().split(" "))
for i in range(1, V+1):
    graph[i] = {}
K = int(input())
for i in range(E):
    u, v, w = map(int, input().split(" "))
    if v in graph[u].keys():
        graph[u][v] = min(graph[u][v], w)
    else :
        graph[u][v] = w

# 최단거리 계산
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함. 큐에 답는 값은 [현재까지 이동 거리, 현재 위치(가장 최근의 도착지)]

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] >= current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances
distances = dijkstra(graph, K)

# 출력
print("\n".join(map(lambda x: str(x).upper(), list(distances.values()))))