# Filling the Graph (based on the image)

graph: dict[str, dict[str, int]] = {}

graph["book"] = {} # start node
graph["book"]["lp"] = 5
graph["book"]["poster"] = 0

graph["lp"] = {}
graph["lp"]["guitar"] = 15
graph["lp"]["drums"] = 20

graph["poster"] = {}
graph["poster"]["guitar"] = 30
graph["poster"]["drums"] = 35

graph["guitar"] = {}
graph["guitar"]["piano"] = 20

graph["drums"] = {}
graph["drums"]["piano"] = 10

graph["piano"] = {}  # finish node


# Costs (In this list its not attributed the fist node because it doesnt cost nothing to get there!)
# How much i need to get to that specific node, if its beyound the first neighbors i set to Infinity!
infinity = float("inf")

costs: dict[str, float] = {}
costs["lp"] = 5
costs["poster"] = 0
costs["guitar"] = infinity
costs["drums"] = infinity
costs["piano"] = infinity


# Parents

parents: dict[str, str | None] = {}
parents["lp"] = "book"
parents["poster"] = "book"
parents["guitar"] = None
parents["drums"] = None
parents["piano"] = None


# Processed

processed: list[str] = []


def find_lowest_cost_node(costs: dict[str, float]) -> str | None:
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:

        cost = costs[node]
        

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


if __name__ == "__main__":
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors:
            new_cost = cost + neighbors[n] # if it's cheaper to get to this neighbor by going through this node
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)

    print("Final costs:", costs)
    print("Parents:", parents)
    print('Processed Nodes: ', processed)
