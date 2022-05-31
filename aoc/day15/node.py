class Node:
    def __init__(self, position):
        self.position = position
        self.risk = 0
    
    def determine_next_nodes(self, maze_length, resolution):
        nodes = []
        if self.position % resolution:
            nodes.append(Node(self.position - 1))
        if self.position % resolution < resolution - 1:
            nodes.append(Node(self.position + 1))
        if self.position > resolution:
            nodes.append(Node(self.position - resolution))
        if self.position < maze_length - resolution:
            nodes.append(Node(self.position + resolution))
        return nodes

    def __eq__(self, node):
        return self.position == node.position

    def __lt__(self, node):
        return self.risk < node.risk