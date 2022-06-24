import networkx as nx
import random


# open file to append graphs
output_file = open("graphs.txt", "a")


#####################################################################################################
#                                                                                                   #
#                Randomly generating directed graphs with order within given range                  #
#                                                                                                   #
#####################################################################################################


# adding another graph to file
# input: minimum and maximum order of graph (integer each), minimum and maximum probability to have edge between vertices (float between 0 an 1 each)
def append_graph(min_order, max_order, min_p, max_p):
    
    # get random graph order
    n = random.randrange(min_order, max_order + 1)
    
    # print(n) # nice for running script to check output 

    # random likilihood to create edges
    p = random.randrange(min_p, max_p + 1)

    # create directed graph
    D = nx.gnp_random_graph(n, p/100.0, directed=True)

    # write graph order to file
    output_file.write(str(n) + '\n')
    
    # write adjacency list to file
    for u in range(n):
        for v in D[u]:
            output_file.write(str(v) + ' ')
        output_file.write('\n')


# main where multiple graphs get written to file
for i in range(0, 10):
    append_graph(5, 50, 30, 40)
output_file.write('0\n') #closing output with 0


#closing file
output_file.close()



        
