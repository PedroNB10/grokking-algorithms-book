from __future__ import annotations


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors: dict[Node, int] = {}

    def connect(self, neighbor: Node, weight: int) -> None:
        self.neighbors[neighbor] = weight

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Node) and self.name == other.name

    def __repr__(self) -> str:
        return f"Node({self.name!r})"


def collect_nodes(start: Node) -> set[Node]:
    visited: set[Node] = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        stack.extend(current.neighbors.keys())

    return visited


def find_lowest_cost_node(costs: dict[Node, float], processed: set[Node]) -> Node | None:
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra(start: Node) -> tuple[dict[Node, float], dict[Node, Node | None]]:
    infinity = float("inf")
    all_nodes = collect_nodes(start)

    costs: dict[Node, float] = {node: infinity for node in all_nodes if node is not start}
    parents: dict[Node, Node | None] = {node: None for node in all_nodes if node is not start}

    for neighbor, weight in start.neighbors.items():
        costs[neighbor] = weight
        parents[neighbor] = start

    processed: set[Node] = set()
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]

        for neighbor, weight in node.neighbors.items():
            new_cost = cost + weight
            if new_cost < costs.get(neighbor, infinity):
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.add(node)
        node = find_lowest_cost_node(costs, processed)

    return costs, parents


def reconstruct_path(parents: dict[Node, Node | None], start: Node, end: Node) -> list[str]:
    if end not in parents:
        return []

    path = [end.name]
    current = end

    while current != start:
        parent = parents.get(current)
        if parent is None:
            return []
        path.append(parent.name)
        current = parent

    path.reverse()
    return path


if __name__ == "__main__":
    book = Node("book")
    lp = Node("lp")
    poster = Node("poster")
    guitar = Node("guitar")
    drums = Node("drums")
    piano = Node("piano")

    book.connect(lp, 5)
    book.connect(poster, 0)

    lp.connect(guitar, 15)
    lp.connect(drums, 20)

    poster.connect(guitar, 30)
    poster.connect(drums, 35)

    guitar.connect(piano, 20)
    drums.connect(piano, 10)

    costs, parents = dijkstra(book)

    readable_costs = {node.name: cost for node, cost in costs.items()}
    readable_parents = {node.name: (parent.name if parent else None) for node, parent in parents.items()}
    path_to_piano = reconstruct_path(parents, book, piano)

    print("Final costs:", readable_costs)
    print("Parents:", readable_parents)
    print("Path to piano:", " -> ".join(path_to_piano))