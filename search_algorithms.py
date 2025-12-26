from collections import deque
import heapq

def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        visited.add((x, y))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and
                maze[ny][nx] not in ['X', 'E'] and (nx, ny) not in visited):
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and
                maze[ny][nx] not in ['X', 'E'] and (nx, ny) not in visited):
                stack.append(((nx, ny), path + [(nx, ny)]))
    return []

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start, [start]))
    g_costs = {start: 0}
    visited = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == end:
            return path

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            next_node = (nx, ny)
            if (0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and
                maze[ny][nx] not in ['X', 'E']):
                new_cost = g_costs[current] + 1
                if next_node not in g_costs or new_cost < g_costs[next_node]:
                    g_costs[next_node] = new_cost
                    priority = new_cost + heuristic(next_node, end)
                    heapq.heappush(open_set, (priority, next_node, path + [next_node]))
    return []
