"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import simpleplot
import math
import random

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(40)


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


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes and returns a dictionary
    corresponding to a complete directed graph with the 
    specified number of nodes. 
    
    A complete graph has all possible edges excluding self-loops.
    The nodes of the graph should be numbered 0 to num_nodes - 1
    when num_nodes is positive. Otherwise, the function returns
    a dictionary corresponding to the empty graph.
    """
    
    computed_graph = {}
    vertex_set = set(range(num_nodes))
    
    for ver in vertex_set:
        temp = vertex_set.copy()
        temp.remove(ver)
        computed_graph[ver] = set(temp)
        
    return computed_graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph/digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph. 
    
    The function returns a dictionary with the same set of keys(nodes)
    as digraph whose corresponding values are the number of edges 
    whose head matches a particular node.
    """
    
    in_degree = {}
    vertex_set = digraph.keys()
    
    for ver in vertex_set:
        in_degree[ver] = 0
        
    for ver in vertex_set:
        for ele in digraph[ver]:
            try:
                in_degree[ele] += 1
            except:
                pass
            
    return in_degree


def in_degree_distribution(digraph):
    """
    Takes a directed graph (represented as a dictionary) and computes
    the unnormalized distribution of the in-degrees of graph. 
    
    The function returns a dictionary whose keys correspond to the
    in-degrees of nodes in the graph. 
    
    The value associated with each particular in-degree is the 
    number of nodes with that in-degree. 
    In-degrees with no corresponding nodes in the graph are not 
    included in the dictionary.
    """
    
    in_degree = compute_in_degrees(digraph)
    vertex_set = in_degree.keys()
    degree_dist = {}
    
    for ver in vertex_set:
        degree_value = in_degree[ver]
        
        if degree_dist.has_key(degree_value):
            degree_dist[degree_value] += 1
        else:
            degree_dist[degree_value] = 1
            
    return degree_dist

def make_ER(num_nodes, probability):
    
    computed_graph = {}
    vertex_set = set(range(num_nodes))
    
    for ver in vertex_set:
        a = random.random()
        if a < probability:
            temp = vertex_set.copy()
            temp.remove(ver)
            computed_graph[ver] = set(temp)
        
    return computed_graph

def print_distro(digraph):
    dataset = in_degree_distribution(digraph)
    dataset1 = []
    normalizing_factor = 0
    for key in dataset:
        normalizing_factor += dataset[key]

    normalizing_factor = math.log(normalizing_factor,10)

    for key in dataset:
        dataset1.append((math.log(key,10),(math.log(dataset[key],10)-normalizing_factor)))

    heading = "Log/Log plot of in_degree distribution for citation graph"
    y_label = "Fraction of Papers (log with base 10)"
    x_label = "Number of Citations (log with base 10)"

    simpleplot.plot_scatter(heading, 800, 600, x_label, y_label, [dataset1], ['Citation Graph'])
    


citation_graph = load_graph(CITATION_URL)
er_graph = make_ER(27770,0.005)

print_distro(citation_graph)
#print_distro(er_graph)


