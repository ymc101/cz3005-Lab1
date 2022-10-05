import json
import ucsnocost
import ucsfull
import astar
import timeit

def main():
    #initialization: opens all json files and return data as dictionary
    with open('data/G.json', 'r') as graph_file:
        graphdata = json.load(graph_file)

    with open("data/Dist.json", "r") as dist_file:
        distdata = json.load(dist_file)

    with open('data/Cost.json', "r") as cost_file:
        costdata = json.load(cost_file)

    with open('data/Coord.json', "r") as coord_file:
        coorddata = json.load(coord_file)

    startnode = "1"
    endnode = "50"
    costbudget = 287932
    print("Running Task 1: relaxed NYC instance with no cost\nUsing Uniform Cost Search (UCS) algorithm\n")
    print(f"Start node: {startnode}")
    print(f"End node: {endnode}")
    time_for_ucsnocost = timeit.timeit(lambda: ucsnocost.ucsnocost(startnode, endnode, graphdata, distdata, costdata), number=1)
    print(f"Time taken for UCS no cost: {time_for_ucsnocost}")
    print("\n")

    print("Running Task 2: full NYC instance\nUsing uninformed search algorithm: Uniform Cost Search (UCS)\n")
    print(f"Start node: {startnode}")
    print(f"End node: {endnode}")
    print(f"Energy cost budget: {costbudget}\n")
    time_for_ucsfull = timeit.timeit(lambda: ucsfull.ucsfull(startnode, endnode, graphdata, distdata, costdata, costbudget), number=1)
    print(f"Time taken for UCS full cost: {time_for_ucsfull}")
    print("\n")

    print("Running Task 3: full NYC instance\nUsing informed search algorithm: A Star Search\n")
    print(f"Start node: {startnode}")
    print(f"End node: {endnode}")
    print("Heuristic function: Displacement from current node to goal node")
    print(f"Energy cost budget: {costbudget}\n")
    astar.astar(startnode, endnode, graphdata, distdata, costdata, costbudget, coorddata)


if __name__ == "__main__":
    main()
