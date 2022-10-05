from queue import PriorityQueue
from math import sqrt

def astar(start, end, graph, distance, cost, costbudget, coord):
    #initialization
    dist_from_source = {start:0}
    cost_from_source = {start:0}
    visitednodes = []
    pqueue=PriorityQueue()
    #heuristic: displacement from current to end node
    #evaluation function is 
    evaluation = 0 + sqrt((coord[start][0]-coord[end][0])**2 + (coord[start][1]-coord[end][1])**2)
    evallist = {start:evaluation}
    pqueue.put((evaluation, start))
    parent = {}
    while len(pqueue.queue)>0:
        cur=pqueue.get()[1]
        visitednodes.append(cur)
        #goal checking
        if cur==end:
            solutionpath = [end]
            pathbacktracker = end
            while True: #iterate through parent list to obtain solution path
                pathbacktracker = parent[pathbacktracker]
                solutionpath.append(pathbacktracker)
                if pathbacktracker==start:
                    solutionpath.reverse()
                    break
            #print results
            print("Shortest path:")
            for node in solutionpath:
                if node == start:
                    print("S", end='')
                elif node == end:
                    print("T", end='')
                else:
                    print(f"{node}", end='')
                if node!=end:
                    print("->", end='')
            print(f"\nShortest distance: {dist_from_source[end]}")
            print(f"Total energy cost: {cost_from_source[end]}")
            return None

        #else expand node
        for neighbour in graph[cur]:
            dist = dist_from_source[cur] + distance[f'{cur},{neighbour}']
            newevaluation = dist + sqrt((coord[neighbour][0]-coord[end][0])**2 + (coord[neighbour][1]-coord[end][1])**2)
            newcost = cost_from_source[cur] + cost[f'{cur},{neighbour}']
            if (neighbour not in visitednodes or evallist[neighbour] > newevaluation) and newcost<costbudget:
            #if neighbour is newly encountered node or path through current node to neighbour is shorter than recorded shortest path to neighbour
            #if cumulative energy cost exceeds budget, do not consider this neighbour
                if neighbour not in visitednodes: #mark neighbour as visited
                    visitednodes.append(neighbour)
                pqueue.put((newevaluation, neighbour))
                evallist[neighbour] = newevaluation
                dist_from_source[neighbour] = dist
                cost_from_source[neighbour] = newcost
                parent[neighbour] = cur

    return None