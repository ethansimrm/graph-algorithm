"""
Project 1: Degree Distributions for Graphs
"""

## Constants

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 
             2: set([3]), 3: set([0]), 4: set([1]), 
             5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]),
             2: set([3, 7]), 3: set([7]), 
             4: set([1]), 5: set([2]), 6: set([]), 
             7: set([3]), 8: set([1, 2]), 
             9: set([0, 3, 4, 5, 6, 7])} 
 
def make_complete_graph(num_nodes):
    """
    Generates a complete digraph for a given number
    of nodes.
    
    Returns digraph in dictionary form.
    """
    ans_dict = {}
    if num_nodes > 0:
        for node in range(num_nodes):
            ans_dict[node] = set([])
            for tail in range(num_nodes):
                if tail != node:
                    ans_dict[node].add(tail)
    return ans_dict

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph and 
    computes in-degrees for nodes.
    
    Returns a dictionary with same set of keys; values
    are their in-degrees.
    """
    ans_dict = {}
    for node in digraph.keys():
        ans_dict[node] = 0
    for tail_node_set in digraph.values():
        for tail_node in tail_node_set:
            ans_dict[tail_node] += 1
    return ans_dict

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph and returns
    dictionary with indegrees as keys and number of 
    nodes with said indegree as values.
    """
    ans_dict = {}
    in_degree_dict = compute_in_degrees(digraph)
    in_degree_set = set(in_degree_dict.values())
    for in_degree in in_degree_set:
        ans_dict[in_degree] = 0
        for node in in_degree_dict.keys():
            if in_degree_dict[node] == in_degree:
                ans_dict[in_degree] += 1
    return ans_dict
    

#print make_complete_graph(4)
#print compute_in_degrees(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH1)

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#citation_graph = load_graph(CITATION_URL)

## Question 1
import simpleplot
import math

#in_degree_data = in_degree_distribution(citation_graph)

# Normalize

def normalize(dictionary):
    """
    Normalize values in dictionary such that they sum to 1.
    """
    num_nodes = 0
    for value in dictionary.values():
        num_nodes += value
    for key in dictionary.keys():
        dictionary[key] = float(dictionary[key]) / num_nodes
    return dictionary

#norm_data = normalize(in_degree_data)

# Plotting function

def build_plot(plot_dict, plot_type = True):
    """
    Build plot of dictionary
    """
    plot = []
    for input_val in plot_dict.items():
        if plot_type:
            plot.append((input_val[0], input_val[1]))
        else:
            if input_val[0] != 0:
                plot.append((math.log(input_val[0]), math.log(input_val[1])))
    return plot

#plot1 = build_plot(norm_data, False)
#print plot1

#simpleplot.plot_scatter("Log-Log Plot of Normalized Citation Graph In-degree Distribution", 600, 600, 
#                        "Natural Logarithm of Citation Graph in-degrees", 
#                        "Natural Logarithm of Normalized N(nodes)", 
#                        [plot1])

## Question 2
import random

# Algorithm ER implementation

def ER(num_nodes, prob):
    ans_dict = {}
    for node in range(num_nodes):
        ans_dict[node] = set([])
        for tail_node in range(num_nodes):
            if node != tail_node:
                a = random.random()
                if a < prob:
                    ans_dict[node].add(tail_node)
    return ans_dict

#ER_data1 = normalize(in_degree_distribution(ER(1000, 0.05)))
#ER_data2 = normalize(in_degree_distribution(ER(1000, 0.5)))
#ER_data3 = normalize(in_degree_distribution(ER(1000, 0.95)))

#plot2 = build_plot(ER_data1, False)
#plot3 = build_plot(ER_data2, False)
#plot4 = build_plot(ER_data3, False)
#
#simpleplot.plot_scatter("Log-Log Plot of Normalized ER Graph In-degree Distribution", 600, 600, 
#                        "Natural Logarithm of ER Graph in-degrees", 
#                        "Natural Logarithm of Normalized N(nodes)", 
#                        [plot2, plot3, plot4])

## Question 4
import alg_dpa_trial as provided

# Seems like the DPA algorithm generates a complete digraph, and slowly builds
# towards the 27770-node graph node by node;
# each node adds edges in steps of 13 (avg outdegree).

def dpa(num_nodes, final_nodes):
    complete_dpa = provided.DPATrial(num_nodes)
    ans_dict = make_complete_graph(num_nodes)
    for node in range(num_nodes, final_nodes):
        new_neighs = complete_dpa.run_trial(num_nodes)
        ans_dict[node] = set([])
        for neigh in new_neighs:
            ans_dict[node].add(neigh) 
    return ans_dict

dpa_graph = dpa(13, 27770)
dpa_data = normalize(in_degree_distribution(dpa_graph))

#plot5 = build_plot(dpa_data, False)
#simpleplot.plot_scatter("Log-Log Plot of Normalized DPA Graph In-degree Distribution", 600, 600, 
#                        "Natural Logarithm of DPA Graph in-degrees", 
#                        "Natural Logarithm of Normalized N(nodes)", 
#                        [plot5])
