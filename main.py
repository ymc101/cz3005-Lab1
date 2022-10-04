import json
import ucsnocost
import ucsfull
import astar

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
    ucsnocost.ucsnocost(startnode, endnode, graphdata, distdata, costdata)
    print("\n")

    print("Running Task 2: full NYC instance\nUsing uninformed search algorithm: Uniform Cost Search (UCS)\n")
    print(f"Start node: {startnode}")
    print(f"End node: {endnode}")
    print(f"Energy cost budget: {costbudget}\n")
    ucsfull.ucsfull(startnode, endnode, graphdata, distdata, costdata, costbudget)
    print("\n")

    print("Running Task 3: full NYC instance\nUsing informed search algorithm: A Star Search\n")
    print(f"Start node: {startnode}")
    print(f"End node: {endnode}")
    print(f"Energy cost budget: {costbudget}\n")
    astar.astar(startnode, endnode, graphdata, distdata, costdata, coorddata, costbudget)


if __name__ == "__main__":
    main()
