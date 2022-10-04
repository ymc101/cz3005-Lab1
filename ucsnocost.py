from queue import PriorityQueue

def ucsnocost(start, end, graph, distance, cost):
    #initialization
    dist_from_source = {start:0}
    cost_from_source = {start:0}
    visitednodes = []
    pqueue=PriorityQueue()
    pqueue.put((0, start))
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
            if neighbour not in visitednodes or dist_from_source[neighbour] > dist: 
                #if neighbour is newly encountered node or path through current node to neighbour is shorter than recorded shortest path
                if neighbour not in visitednodes: #mark neighbour as visited
                    visitednodes.append(neighbour)
                pqueue.put((dist, neighbour))
                dist_from_source[neighbour] = dist
                cost_from_source[neighbour] = cost_from_source[cur] + cost[f'{cur},{neighbour}']
                parent[neighbour] = cur

    return None