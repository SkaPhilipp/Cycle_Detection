import sys


#####################################################################################################
#                                                                                                   #
#                                      Read adjacency list from input                               #
#                                                                                                   #
#####################################################################################################

# read adjacency list from standard input
# input: order of graph (integer)
def read_adjacency_list(order):
    adjacency_list = []

    # read single adjacency list from stdinput and store as list of lists
    for _ in range(order):
        index = sys.stdin.readline().strip()
        adjacency_list.append([int(vertex) for vertex in index.split()])

    return adjacency_list


#####################################################################################################
#                                                                                                   #
#                          Recursive Depth First Search implementation                              #
#                                                                                                   #
#####################################################################################################


# recursive implementation of Depth First Search algorithm
# input: vertex sto start recursive search
def recursiveDFSvisit(s):

    # mark first visited vertex as visited / gray
    colour[s] = 'G'

    # set timestamp for vertex s
    seen[s] = time[0]

    # increase timestampe
    time[0] += 1

    # visit outneighbors of vertex s
    for v in adjacency_list[s]:

        # if outneighbor v is not visited / white then perform recursive DFS visit
        if colour[v] == 'W':
            pred[v] = s
            recursiveDFSvisit(v)

    # mark vertex s as finsihed / black and increase timestamp
    colour[s] = 'B'
    done[s] = time[0]
    time[0] += 1


#####################################################################################################
#                                                                                                   #
#                          Main function running DFS and detecting cycles                           #
#                                                                                                   #
#####################################################################################################


# main function to run DFS and detect cycles

# initialise graph number
graph_number = 0

# read first integer as order for following graph given as adjacency list
order = int(sys.stdin.readline().strip())

# open output file where result is stored whether graph contains cycle
output_file = open("cycle_dection.txt", "a")

while order != 0:

    # write graph number to output file
    graph_number += 1
    output_file.write(f"Graph {graph_number}: ")

    # create adjacency list from input
    adjacency_list = read_adjacency_list(order)

    # initialise DFS arrays
    colour = ['W'] * order
    seen = [None] * order
    done = [None] * order
    pred = [-1] * order
    time = [0]

    # visit all vertices in graph and perform recursive DFS, important in case graph is not strongly connected
    for node in range(len(adjacency_list)):
        if colour[node] == 'W':
            recursiveDFSvisit(node)

    # after running DFS check for back edges to determine whether cycle exists
    back_edge = 0

    for v in range(len(adjacency_list)):
        for w in adjacency_list[v]:
            if seen[w] < seen[v] < done[v] < done[w]:
                back_edge += 1

    # print and add to output file whether cycle detected or not
    if back_edge > 0:
        print("Cycle detected\n")
        output_file.write("Cycle detected\n")
    else:
        print("No cycle detected\n")
        output_file.write("No cycle detected\n")

    # increment graph number counter and read next order or '0' as end of input
    order = int(sys.stdin.readline().strip())

# close file
output_file.close()
    
sys.exit()

