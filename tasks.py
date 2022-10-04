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
Dist = json.load(open("data/Dist.json"))
Cost = json.load(open("data/Cost.json"))

# retrieve test data
G = json.load(open("test_data/G.json"))
Coord = json.load(open("test_data/Coord.json"))
Dist = json.load(open("test_data/Dist.json"))
Cost = json.load(open("test_data/Cost.json"))


def task1():
    # You will need to solve a relaxed version of the NYC instance where we do not have the energy constraint
    return



def task2():
    # You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance
    return


# returns (shortest path, shortest distance, total energy cost)
def task3():
    # You will need to develop an A* search algorithm to solve the NYC instance
    shortest_path = [start]
    shortest_distance = 0
    total_energy_cost = 0

    candidates = []
    for neighbour in G[str(start)]:
        candidates.append({
            "prepath": [start],
            "candidate": int(neighbour),
            "g(n)": Cost[str(start)+","+neighbour],
            "h(n)": Dist[neighbour+","+str(end)],
            "f(n)": Cost[str(start)+","+neighbour] + Dist[neighbour+","+str(end)]
        })
    
    while shortest_path[-1] != end:
        # find candidate with lowest f(n)
        min_f = candidates[0]["f(n)"]
        candidate_index = 0
        for i, candidate in enumerate(candidates):
            if candidate["f(n)"] > min_f:
                min_f = candidate["f(n)"]
                candidate_index = i
        
        # visit candidate, update candidate list
        candidate = candidates[candidate_index]
        for neighbour in G[str(candidate["candidate"])]:
            # add neighbour as new candidate
            prepath = deepcopy(candidate["prepath"])
            prepath.append(candidate["candidate"])
            g_n = candidate["g(n)"] + Cost[str(candidate["candidate"])+","+neighbour]

            candidates.append({
                "prepath": prepath,
                "candidate": int(neighbour),
                "g(n)": g_n,
                "h(n)": Dist[neighbour+","+str(end)],
                "f(n)": g_n + Dist[neighbour+","+str(end)]
            })
    return