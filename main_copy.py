from tasks import task1, task2, task3

def shortest_path_to_string(shortest_path):
    shortest_path_string = ""
    for i in range(len(shortest_path)-1):
        shortest_path_string += str(shortest_path[i]) + "->"
    shortest_path_string += str(shortest_path[len(shortest_path)-1])
    return shortest_path_string


##########
# TASK 1 #
##########





##########
# TASK 2 #
##########





##########
# TASK 3 #
##########
output_task3 = task3()

print("===== Task 3 =====")
print("Shortest path: ", shortest_path_to_string(output_task3[0]))
print("Shortest distance: ", output_task3[1])
print("Total energy cost: ", output_task3[2])

