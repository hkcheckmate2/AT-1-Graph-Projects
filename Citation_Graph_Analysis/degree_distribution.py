"""
Hritvik Kishore
170907150
Degree Distributions for Graphs
"""
import codeskulptor
codeskulptor.set_timeout(100)

#Example Graphs
EX_GRAPH0 = {0: set([1,2]), 
             1: set([]), 
             2: set([])}

EX_GRAPH1 = {0: set([1,4,5]), 
             1:set([2,6]),
             2:set([3]), 
             3:set([0]), 
             4: set([1]),
             5: set([2]), 
             6: set([])}

EX_GRAPH2 = {0: set([1,4,5]), 
             1:set([2,6]),
             2:set([3,7]), 
             3:set([7]), 
             4: set([1]),
             5: set([2]), 
             6: set([]),
             7: set([3]), 
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

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
            in_degree[ele] += 1
            
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
