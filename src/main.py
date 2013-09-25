import itertools
import networkx as nx
from networkx.algorithms import isomorphism, articulation_points

class RigidGraphs:
    def __init__(self):
        self.dc = DeleteContract()
    def sum(self, n):
        s = 0
        for i in xrange(1, n+1):
            for j in xrange(1, n+1):
                s += self.rigid(i, j)
        return s
    def rigid(self, m, n):
        return self.dc.combinations(m,n)

def loops(graph):
    '''Returns list of loops'''
    for e in graph.edges():
        (a, b) = e
        if a == b:
            yield e

#Enumeration Finder
class DeleteContract:
    def __init__(self):
        self.knownGraphs = {}
    def combinations(self, cols, rows):
        ''' Return number of combinations to make rigid graph.'''
        #Setup bipartite graph
        G = nx.Graph()
        rows = ['r' + str(i) for i in xrange(rows)]
        cols = ['c' + str(i) for i in xrange(cols)]
        edges = itertools.product(rows, cols)
        G.add_edges_from(edges)
        print(G.edges())
        return self.calculate(G)
    def calculate(self, graph):
        ''' Return Tutte polynomial at (1,2)'''
        frontier = [graph]
        s = 0
        while len(frontier) > 0:
            G = frontier.pop()
            # If we know result for subtree of G.
            try:
                s += self.getValue(G)
            except KeyError:
                # pick random edge from G.
                bridges = list(articulation_points(G));
                l = list(loops(G))
                if len(l) == 0 and len(bridges) == 0:
                    # Get Ordinary Edge (neither cut nor bridge)
                    e = G.edges()[0]
                    frontier.append(delete(G, e))
                    frontier.append(contract(G, e))
                elif len(bridges) != 0:
                    # Take cut-edges and contract
                    e = bridges[0]
                    frontier.append(contract(G, e)) # TODO: multiply by tutte
                elif len(l) != 0:
                    # take loop and delete
                    e = l[0]
                    frontier.append(delete(G, e)) # TODO: multiply by tutte
        return s
    def getValue(self, graph):
        ''' Lookup polynomial evaluation or calculate value if graph size is 1.'''
        if graph.number_of_edges() == 0:
            return 1
        try:
            for candidate, value in self.knownGraphs[(graph.number_of_edges(), graph.number_of_nodes())]:
                if isomorphism.faster_could_be_isomorphic(candidate, graph):
                    if isomorphism.is_isomorphic(candidate, graph):
                        return value
        except KeyError:
            raise KeyError
    def addGraph(self, graph, value):
        n = graph.number_of_nodes()
        e = graph.number_of_edges()
        if self.knownGraphs.has_key((n, e)):
            self.knownGraphs[(n, e)].append((graph, value))
        else:
            self.knownGraphs[(n, e)] = [(graph, value)]

def delete(graph, edge):
    ''' Take graph, delete edge and return new graph.'''
    g = graph.copy()
    g.remove_edge(*edge)
    return g
def contract(graph, edge):
    '''Take graph, contract edge and return new graph.'''
    g = nx.MultiGraph(graph)
    g.remove_edge(*edge)
    # Move/Copy edges from node1 (= edge[1]) to node0.
    for n, adj in g.adjacency_iter():
        if n == edge[1]:
            for out in adj:
                g.add_edge(edge[0], out)
    # Remove node1
    g.remove_node(edge[1])
    return g

if __name__=='__main__':
    rg = RigidGraphs()
    rg.rigid(3, 2)