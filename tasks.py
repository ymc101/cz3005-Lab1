import json
from copy import deepcopy


# Graph dictionary G
# The graph is given as an adjacency list where the neighbor list of node ‘v’ can be accessed with G[‘v’]

# Node coordination dictionary Coord
# The coordination of a node ‘v’ is a pair (X, Y) which can be accessed with Coord[‘v’]

# Edge distance dictionary Dist
# The distance between a pair of node (v, w) can be accessed with Dist[‘v,w’]

# Edge cost dictionary Cost
# The energy cost between a pair of node (v, w) can be accessed with Cost[‘v,w’]

num_of_nodes = 264346
num_of_edges = 730100
energy_budget = 287932

start = 1
end = 50

# retrieve data
G = json.load(open("data/G.json"))
Coord = json.load(open("data/Coord.json"))
Dist = json.load(open("data/Dist.json")) # float
Cost = json.load(open("data/Cost.json")) # int
'''
# retrieve test data
G = json.load(open("test_data/G.json"))
Coord = json.load(open("test_data/Coord.json"))
Dist = json.load(open("test_data/Dist.json"))
Cost = json.load(open("test_data/Cost.json"))
'''


def task1():
    # You will need to solve a relaxed version of the NYC instance where we do not have the energy constraint
    return



def task2():
    # You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance
    return



# returns (shortest path, shortest distance, total energy cost)
def task3(start = start, end = end, energy_budget = energy_budget):
    # You will need to develop an A* search algorithm to solve the NYC instance
    shortest_path = [start]
    candidates = []

    for neighbour in G[str(start)]:
        h_n = ( ( ( Coord[str(start)][0] - Coord[neighbour][0] ) ** 2 ) + ( ( Coord[str(start)][1] - Coord[neighbour][1] ) ** 2 ) ) ** 0.5
        candidates.append({
            "prepath": [start],
            "candidate": int(neighbour),
            "g(n)": Dist[str(start)+","+neighbour],
            "h(n)": h_n,
            "f(n)": Dist[str(start)+","+neighbour] + h_n,
            "cost": Cost[str(start)+","+neighbour]
        })
    
    while shortest_path[-1] != end:
        print(shortest_path)

        # find candidate with lowest f(n)
        min_f = candidates[0]["f(n)"]
        candidate_index = 0
        for i, candidate in enumerate(candidates):
            if (candidate["f(n)"] < min_f) and (candidate["candidate"] not in shortest_path):
                min_f = candidate["f(n)"]
                candidate_index = i
        
        candidate = candidates[candidate_index]
        shortest_path = deepcopy(candidate["prepath"])
        shortest_path.append(candidate["candidate"])

        # if candidate is the end node, return output
        if shortest_path[-1] == end:
            return (shortest_path, candidate["g(n)"], candidate["cost"])

        # visit candidate, update candidate list
        for neighbour in G[str(candidate["candidate"])]:
            # ignore neighbour already in current path
            if int(neighbour) in shortest_path:
                continue

            # ignore neighbour with potential energy cost > budget
            cost = candidate["cost"] + Cost[str(candidate["candidate"])+","+neighbour]
            if (cost > energy_budget):
                continue

            # add neighbour as new candidate
            g_n = candidate["g(n)"] + Dist[str(candidate["candidate"])+","+neighbour]
            h_n = ( ( ( Coord[str(candidate["candidate"])][0] - Coord[neighbour][0] ) ** 2 ) + ( ( Coord[str(candidate["candidate"])][1] - Coord[neighbour][1] ) ** 2 ) ) ** 0.5

            candidates.append({
                "prepath": shortest_path,
                "candidate": int(neighbour),
                "g(n)": g_n,
                "h(n)": h_n,
                "f(n)": g_n + h_n,
                "cost": cost
            })
        candidates.pop(candidate_index)
    return None