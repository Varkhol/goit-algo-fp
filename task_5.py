import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color(step, total_steps):
    r = int(139 + (255 - 139) * step / total_steps)
    g = int(0 + (179 - 0) * step / total_steps)
    b = int(48 + (204 - 48) * step / total_steps)
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs(root):
    if not root:
        return []

    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs(root):
    if not root:
        return []

    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def visualize_traversal(root, order, title):
    total = len(order)
    for step, node in enumerate(order):
        node.color = generate_color(step, total)

    draw_tree(root, title)


def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS — стек
    dfs_order = dfs(root)
    print("DFS порядок:", [node.val for node in dfs_order])
    visualize_traversal(root, dfs_order, "DFS")

    for node in dfs_order:
        node.color = "skyblue"

    # BFS — черга
    bfs_order = bfs(root)
    print("BFS порядок:", [node.val for node in bfs_order])
    visualize_traversal(root, bfs_order, "BFS")


if __name__ == "__main__":
    main()