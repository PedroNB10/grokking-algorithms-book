

# graph{
#  "start": {
#    "a" : 6
#    "b" : 2
#  },
# 
#  "a" : {
#    "fin": 1
#  },
#  "b" : {
#     "a" : 3
#  }   
# }

# costs {
#   "a" : 6
#   "b" : 2
#  "fin": Infinity
# }


# Filling the Graph

graph: dict[str, dict[str, int]] = {}


graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # The finish node doesn't have any neighbors


# Costs

# Next you need a hash table to store the costs for each node.
# he cost of a node is how long it takes to get to that
# node from the start. You know it takes 2 minutes from
# Start to node B. You know it takes 6 minutes to get to
# node A (although you may ind a path that takes less
# time)

infinity = float("inf")

costs:dict[str, int] = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


# Processed Nodes (nodes that had sometime the least cost)
processed:list[str] = []


def find_lowest_cost_node(costs: dict[str, int]) -> str | None:
    lowest_cost: int = float("inf")
    lowest_cost_node: str | None = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


if __name__ == "__main__":

    node = find_lowest_cost_node(costs)
    # while we have nodes to process

    while node is not None:
        cost = costs[node]
        neighbors = graph[node] # {'a': 3, 'fin': 5}
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
        