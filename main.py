import json
import ucsnocost
import ucsfull

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

    print("Running Task 1: relaxed NYC instance with no cost\nUsing Uniform Cost Search (UCS) algorithm\n")
    ucsnocost.ucsnocost(1, 50, graphdata, distdata)

    print("Running Task 2: full NYC instance\nUsing uninformed search algorithm: Uniform Cost Search (UCS)\n")
    ucsfull.ucsfull(1, 50, graphdata, distdata, costdata)


if __name__ == "__main__":
    main()
