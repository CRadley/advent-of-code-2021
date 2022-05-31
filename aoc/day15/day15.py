from collections import defaultdict
from heapq import heappop, heappush
from .node import Node


def generate_scaled_maze(maze, resolution, scale):
    segmented_maze = [maze[i:i+resolution] for i in range(0, len(maze), resolution)]
    scaled_maze = []
    for row in segmented_maze:
        for i in range(scale):
            for x in row:
                new_value = x + i
                scaled_maze.append(new_value if new_value < 10 else new_value - 9)
    scaled_maze = [v + i if v + i < 10 else v + i - 9 for i in range(scale) for v in scaled_maze]
    scaled_resolution = resolution * scale
    return scaled_maze, scaled_resolution


def scaled_astar(maze, resolution, scale = 1):
    if scale > 1:
        maze, resolution = generate_scaled_maze(maze, resolution, scale)
    start = 0
    end = len(maze) - 1
    start_node = Node(start)
    end_node = Node(end)
    open_nodes = []
    closed_nodes = defaultdict(int)
    heappush(open_nodes, start_node)
    while open_nodes:
        current_node = heappop(open_nodes)
        closed_nodes[current_node.position]
        if current_node == end_node:
            return current_node.risk    
        for node in current_node.determine_next_nodes(len(maze), resolution):
            if node.position in closed_nodes:
                continue
            node.risk = current_node.risk + maze[node.position]
            if node in open_nodes:
                continue
            heappush(open_nodes, node)

def determine_inputs(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        resolution = len(lines[0].strip())
        maze = [int(c) for line in lines for c in line.strip()]
    return maze, resolution