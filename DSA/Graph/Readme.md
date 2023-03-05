## 1. Python program to implement a graph.

Problem Description
The program creates a Graph data structure and allows the user to add vertices and edges to it.

Problem Solution
1. Create a class Graph.
2. Create a class Vertex.
3. Each object of Vertex has two instance variables, key and points_to.
4. key is the value of the Vertex object.
5. points_to is a dictionary with keys being the Vertex objects that the current object points to. Each such Vertex object pointed to by the current object is mapped to the weight of the corresponding directed edge.
6. The class Vertex provides methods to get the key, to add a neighbour, to get all neighbours, to get the weight of a directed edge and to test whether a vertex is a neigbour of the current Vertex object.
7. The class Graph has one instance variable, vertices.
8. vertices is a dictionary that contains vertex values mapped to their corresponding Vertex objects. Each Vertex object also stores the vertex value in its key instance variable.
9. The class Graph provides methods to add a vertex with a given key, get the Vertex object with a given key, test whether a vertex with a given key is in the Graph, add an edge between two vertices given their keys and weight and test whether an edge exists between two vertices given their keys. The __iter__ method is implemented to allow iteration over the Vertex objects in the graph.
10. If whenever edge (u, v) is added to the graph, the reverse edge (v, u) is also added, then this would become the implementation of an undirected graph.

Program/Source Code
Here is the source code of a Python program to implement a graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> [weight]')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    if len(do) == 5:
                        weight = int(do[4])
                        g.add_edge(src, dest, weight)
                    else:
                        g.add_edge(src, dest)
                else:
                    print('Edge already exists.')
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
  ```
Program Explanation
1. An instance of Graph is created.
2. The user is presented with a menu to perform various operations on the graph.
3. The corresponding methods are called to perform each operation.
4. The operations are: add vertex with a given key, add edge from a source vertex to a destination vertex (optionally with weight specified, otherwise weight=1 is assumed) and to display the all vertices and edges in the graph.


## Runtime Test Cases
```
Case 1:
Menu
add vertex <key>
add edge <src> <dest> [weight]
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? display
Vertices: 1 2 
Edges: 
 
What would you like to do? add edge 1 2
What would you like to do? add vertex 3
What would you like to do? display
Vertices: 1 2 3 
Edges: 
(src=1, dest=2, weight=1) 
 
What would you like to do? add edge 1 3
What would you like to do? add edge 3 1
What would you like to do? display
Vertices: 1 2 3 
Edges: 
(src=1, dest=2, weight=1) 
(src=1, dest=3, weight=1) 
(src=3, dest=1, weight=1) 
 
What would you like to do? quit
 
Case 2:
Menu
add vertex <key>
add edge <src> <dest> [weight]
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add edge 1 2
What would you like to do? add edge 2 3
What would you like to do? add edge 4 5
What would you like to do? display
Vertices: 1 2 3 4 5 
Edges: 
(src=1, dest=2, weight=1) 
(src=2, dest=3, weight=1) 
(src=4, dest=5, weight=1) 
 
What would you like to do? add edge 5 4
What would you like to do? display
Vertices: 1 2 3 4 5 
Edges: 
(src=1, dest=2, weight=1) 
(src=2, dest=3, weight=1) 
(src=4, dest=5, weight=1) 
(src=5, dest=4, weight=1) 
 
What would you like to do? quit
```


## 2. Python program to find all connected components using BFS in an undirected graph.

Problem Description
The program creates a graph object and allows the user to find all connected components.

Problem Solution
1. Create classes for Graph, Vertex and Queue.
2. Create a function label_all_reachable that takes a Vertex object, a dictionary called component and a label as argument.
3. The function begins by creating an empty set called visited and a Queue object, q.
4. It enqueues the passed Vertex object and also adds it to the set visited.
5. A while loop is created which runs as long as the queue is no empty.
6. In each iteration of the loop, the queue is dequeued, label is assigned to component[dequeued vertex] and all of its neighbours are enqueued which have not already been visited.
7. In addition to enqueuing, they are also added to the visited set.
8. Thus, after the function is called, each vertex in the connected component containing the source vertex is assigned the given label in the dictionary called component.

Program/Source Code
Here is the source code of a Python program to find all connected components using BFS in an undirected graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def add_undirected_edge(self, v1_key, v2_key, weight=1):
        """Add undirected edge (2 directed edges) between v1_key and v2_key with
        given weight."""
        self.add_edge(v1_key, v2_key, weight)
        self.add_edge(v2_key, v1_key, weight)
 
    def does_undirected_edge_exist(self, v1_key, v2_key):
        """Return True if there is an undirected edge between v1_key and v2_key."""
        return (self.does_edge_exist(v1_key, v2_key)
                and self.does_edge_exist(v1_key, v2_key))
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
def label_all_reachable(vertex, component, label):
    """Set component[v] = label for all v in the component containing vertex."""
    visited = set()
    q = Queue()
    q.enqueue(vertex)
    visited.add(vertex)
    while not q.is_empty():
        current = q.dequeue()
        component[current] = label
        for dest in current.get_neighbours():
            if dest not in visited:
                visited.add(dest)
                q.enqueue(dest)
 
 
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest>')
print('components')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_undirected_edge_exist(src, dest):
                    g.add_undirected_edge(src, dest)
                else:
                    print('Edge already exists.')
 
    elif operation == 'components':
        component = dict.fromkeys(g, None)
        label = 1
        for v in g:
            if component[v] is None:
                label_all_reachable(v, component, label)
                label += 1
 
        max_label = label
        for label in range(1, max_label):
            component_vertices = [v.get_key() for v in component
                                  if component[v] == label]
            print('Component {}:'.format(label), component_vertices)
 
 
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
 ```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To find all connected components, a dictionary called component is created that contains all Vertex objects in the graph as keys and all of which are mapped to None.
4. Then for each Vertex object v in the graph, if v is mapped to None, label_all_reachable is called on that vertex with a given label. The value of the label is incremented for the next iteration of the loop.
5. The vertices in each component is then displayed.


## Runtime Test Cases
```
Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest>
components
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? components
Component 1: [1]
Component 2: [2]
Component 3: [3]
Component 4: [4]
Component 5: [5]
What would you like to do? add edge 1 2
What would you like to do? add edge 3 4
What would you like to do? components
Component 1: [2, 1]
Component 2: [4, 3]
Component 3: [5]
What would you like to do? add edge 5 1
What would you like to do? add edge 4 2
What would you like to do? components
Component 1: [5, 2, 4, 1, 3]
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest>
components
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add edge 1 2
What would you like to do? add edge 2 3
What would you like to do? add vertex 4
Vertex already exists.
What would you like to do? components
Component 1: [2, 3, 1]
Component 2: [4]
What would you like to do? quit
```

## 3. Python program to find a minimum spanning tree of an undirected weighted graph using Krusal’s algorithm.

Problem Description
A spanning tree of a graph can be defined as a graph with minimal set of edges that connect all vertices. A minimum spanning tree of a graph is a spanning tree of the graph with least weight (where the weight is computed by adding the weights of all the edges in the spanning tree). In general, a graph can have multiple minimum spanning trees. The problem is to find a minimum spanning tree of a graph.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function mst_krusal that takes a Graph object g as argument.
3. The function will return a Graph object which is a minimum spanning tree of the graph g.
4. An empty graph called mst is created which will hold a MST of the graph g.
5. The algorithm works by first sorting all the edges of g in ascending order by weight.
6. Then the smallest edge is taken from the sorted list.
7. If that edge does not form a cycle when added to mst, it is added.
8. Then the next smallest edge is taken and step 7 is performed again.
9. The above is performed until mst has the same number of vertices as g.
10. To determine whether adding an edge will form a cycle, each vertex in g is assigned a component.
11. When any vertex is added to the MST, its component is updated.
12. If both vertices of an edge belong to the same component, then adding the edge will form a cycle.

Program/Source Code
Here is the source code of a Python program to find the minimum spanning tree of an undirected weighted graph using Krusal’s algorithm. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_vertex_exist(self, key):
        return key in self.vertices
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def display(self):
        print('Vertices: ', end='')
        for v in self:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def mst_krusal(g):
    """Return a minimum cost spanning tree of the connected graph g."""
    mst = Graph() # create new Graph object to hold the MST
 
    if len(g) == 1:
        u = next(iter(g)) # get the single vertex
        mst.add_vertex(u.get_key()) # add a copy of it to mst
        return mst
 
    # get all the edges in a list
    edges = []
    for v in g:
        for n in v.get_neighbours():
            # avoid adding two edges for each edge of the undirected graph
            if v.get_key() < n.get_key():
                edges.append((v, n))
 
    # sort edges
    edges.sort(key=lambda edge: edge[0].get_weight(edge[1]))
 
    # initially, each vertex is in its own component
    component = {}
    for i, v in enumerate(g):
        component[v] = i
 
    # next edge to try
    edge_index = 0
 
    # loop until mst has the same number of vertices as g
    while len(mst) < len(g):
        u, v = edges[edge_index]
        edge_index += 1
 
        # if adding edge (u, v) will not form a cycle
        if component[u] != component[v]:
 
            # add to mst
            if not mst.does_vertex_exist(u.get_key()):
                mst.add_vertex(u.get_key())
            if not mst.does_vertex_exist(v.get_key()):
                mst.add_vertex(v.get_key())
            mst.add_edge(u.get_key(), v.get_key(), u.get_weight(v))
            mst.add_edge(v.get_key(), u.get_key(), u.get_weight(v))
 
            # merge components of u and v
            for w in g:
                if component[w] == component[v]:
                    component[w] = component[u]
 
    return mst
 
 
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'mst':
        mst = mst_krusal(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()
 
    elif operation == 'display':
        g.display()
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. mst_krusal is called to get a minimum spanning tree of the graph.
4. This is then displayed.

## Runtime Test Cases
```

Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add edge 1 2 10
What would you like to do? add edge 1 5 30
What would you like to do? add edge 1 4 40
What would you like to do? add edge 2 5 20
What would you like to do? add edge 4 5 40
What would you like to do? add edge 5 3 40
What would you like to do? add edge 5 6 70
What would you like to do? add edge 3 6 50
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 4 5 6 
Edges: 
(src=1, dest=4, weight=40) 
(src=1, dest=2, weight=10) 
(src=2, dest=5, weight=20) 
(src=2, dest=1, weight=10) 
(src=3, dest=5, weight=40) 
(src=3, dest=6, weight=50) 
(src=4, dest=1, weight=40) 
(src=5, dest=2, weight=20) 
(src=5, dest=3, weight=40) 
(src=6, dest=3, weight=50) 
 
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add edge 1 2 10
What would you like to do? add edge 1 3 20
What would you like to do? add edge 2 3 30
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 
Edges: 
(src=1, dest=3, weight=20) 
(src=1, dest=2, weight=10) 
(src=2, dest=1, weight=10) 
(src=3, dest=1, weight=20) 
 
What would you like to do? quit
```
## 4. Python program to find a minimum spanning tree of an undirected weighted graph using Prim’s algorithm.

Problem Description
A spanning tree of a graph can be defined as a graph with minimal set of edges that connect all vertices. A minimum spanning tree of a graph is a spanning tree of the graph with least weight (where the weight is computed by adding the weights of all the edges in the spanning tree). In general, a graph can have multiple minimum spanning trees. The problem is to find a minimum spanning tree of a graph.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function mst_prim that takes a Graph object g as argument.
3. The function will return a Graph object which is a minimum spanning tree of the graph g.
4. An empty graph called mst is created which will hold a MST of the graph g.
5. The algorithm works by selecting any one vertex from g and adding it to mst.
6. The vertex which is outside mst but has a neighbour in mst with the smallest distance is added to mst. (If there are multiple such vertices then add any one.)
7. The corresponding edge is also added.
8. The above two steps are repeated until all vertices have been added to the graph.
9. Two dictionaries are used in the above algorithm.
10. The nearest neighbour in mst of a vertex outside mst is kept track of using a dictionary nearest_neighbour.
11. The corresponding smallest distance is stored in a dictionary called smallest_distance.

Program/Source Code
Here is the source code of a Python program to find the minimum spanning tree of an undirected weighted graph using Prim’s algorithm. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def display(self):
        print('Vertices: ', end='')
        for v in self:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def mst_prim(g):
    """Return a minimum cost spanning tree of the connected graph g."""
    mst = Graph() # create new Graph object to hold the MST
 
    # if graph is empty
    if not g:
        return mst
 
    # nearest_neighbour[v] is the nearest neighbour of v that is in the MST
    # (v is a vertex outside the MST and has at least one neighbour in the MST)
    nearest_neighbour = {}
    # smallest_distance[v] is the distance of v to its nearest neighbour in the MST
    # (v is a vertex outside the MST and has at least one neighbour in the MST)
    smallest_distance = {}
    # v is in unvisited iff v has not been added to the MST
    unvisited = set(g)
 
    u = next(iter(g)) # select any one vertex from g
    mst.add_vertex(u.get_key()) # add a copy of it to the MST
    unvisited.remove(u)
 
    # for each neighbour of vertex u
    for n in u.get_neighbours():
        if n is u:
            # avoid self-loops
            continue
        # update dictionaries
        nearest_neighbour[n] = mst.get_vertex(u.get_key())
        smallest_distance[n] = u.get_weight(n)
 
    # loop until smallest_distance becomes empty
    while (smallest_distance):
        # get nearest vertex outside the MST
        outside_mst = min(smallest_distance, key=smallest_distance.get)
        # get the nearest neighbour inside the MST
        inside_mst = nearest_neighbour[outside_mst]
 
        # add a copy of the outside vertex to the MST
        mst.add_vertex(outside_mst.get_key())
        # add the edge to the MST
        mst.add_edge(outside_mst.get_key(), inside_mst.get_key(),
                     smallest_distance[outside_mst])
        mst.add_edge(inside_mst.get_key(), outside_mst.get_key(),
                     smallest_distance[outside_mst])
 
        # now that outside_mst has been added to the MST, remove it from our
        # dictionaries and the set unvisited
        unvisited.remove(outside_mst)
        del smallest_distance[outside_mst]
        del nearest_neighbour[outside_mst]
 
        # update dictionaries
        for n in outside_mst.get_neighbours():
            if n in unvisited:
                if n not in smallest_distance:
                    smallest_distance[n] = outside_mst.get_weight(n)
                    nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())
                else:
                    if smallest_distance[n] > outside_mst.get_weight(n):
                        smallest_distance[n] = outside_mst.get_weight(n)
                        nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())
 
    return mst
 
 
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'mst':
        mst = mst_prim(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()
 
    elif operation == 'display':
        g.display()
        print()
 
    elif operation == 'quit':
        break
  ```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. mst_prim is called to get a minimum spanning tree of the graph.
4. This is then displayed.


## Runtime Test Cases

```

Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add vertex 7
What would you like to do? add edge 1 3 18
What would you like to do? add edge 1 2 10
What would you like to do? add edge 3 4 70
What would you like to do? add edge 3 2 6
What would you like to do? add edge 2 5 20
What would you like to do? add edge 5 6 10
What would you like to do? add edge 5 7 10
What would you like to do? add edge 6 7 5
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 4 5 6 7 
Edges: 
(src=1, dest=2, weight=10) 
(src=2, dest=5, weight=20) 
(src=2, dest=1, weight=10) 
(src=2, dest=3, weight=6) 
(src=3, dest=2, weight=6) 
(src=3, dest=4, weight=70) 
(src=4, dest=3, weight=70) 
(src=5, dest=6, weight=10) 
(src=5, dest=2, weight=20) 
(src=6, dest=5, weight=10) 
(src=6, dest=7, weight=5) 
(src=7, dest=6, weight=5) 
 
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add edge 1 2 10
What would you like to do? add edge 2 3 100
What would you like to do? add edge 1 3 50
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 
Edges: 
(src=1, dest=2, weight=10) 
(src=1, dest=3, weight=50) 
(src=2, dest=1, weight=10) 
(src=3, dest=1, weight=50) 
 
What would you like to do? quit

```
## 5.Python program to implement Dijkstra’s Shortest Path algorithm on a graph.

Problem Description
The problem is to find the shortest distance to all vertices from a source vertex in a weighted graph.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function dijkstra that takes a Graph object and a source vertex as arguments.
3. The function begins by creating a set unvisited and adding all the vertices in the graph to it.
4. A dictionary distance is created with keys as the vertices in the graph and their value all set to infinity.
5. distance[source] is set to 0.
6. The algorithm proceeds by finding the vertex that has the minimum distance in the set unvisited.
7. It then removes this vertex from the set unvisited.
8. Then all the neighbours of this vertex that have not been visited yet have their distances updated.
9. The above steps repeat until the set unvisited becomes empty.
10. The dictionary distance is returned.
11. This algorithm works for both undirected and directed graphs.

Program/Source Code
Here is the source code of a Python program to implement Dijkstra’s Shortest Path algorithm on a graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def dijkstra(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object.
    source is a Vertex object in g.
    """
    unvisited = set(g)
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
 
    while unvisited != set():
        # find vertex with minimum distance
        closest = min(unvisited, key=lambda v: distance[v])
 
        # mark as visited
        unvisited.remove(closest)
 
        # update distances
        for neighbour in closest.get_neighbours():
           if neighbour in unvisited:
               new_distance = distance[closest] + closest.get_weight(neighbour)
               if distance[neighbour] > new_distance:
                   distance[neighbour] = new_distance
 
    return distance
 
 
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('shortest <source vertex key>')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'shortest':
        key = int(do[1])
        source = g.get_vertex(key)
        distance = dijkstra(g, source)
        print('Distances from {}: '.format(key))
        for v in distance:
            print('Distance to {}: {}'.format(v.get_key(), distance[v]))
        print()
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To find all shortest distances from a source vertex, dijkstra is called on the graph and the source vertex.



## Runtime Test Cases
```
Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
shortest <source vertex key>
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add vertex 7
What would you like to do? add edge 1 2 10
What would you like to do? add edge 1 3 80
What would you like to do? add edge 3 4 70
What would you like to do? add edge 2 5 20
What would you like to do? add edge 2 3 6
What would you like to do? add edge 5 6 50
What would you like to do? add edge 5 7 10
What would you like to do? add edge 6 7 5
What would you like to do? shortest 1
Distances from 1: 
Distance to 6: 45
Distance to 3: 16
Distance to 4: 86
Distance to 5: 30
Distance to 2: 10
Distance to 7: 40
Distance to 1: 0
 
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
shortest <source vertex key>
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add edge 1 2 10
What would you like to do? add edge 2 3 20
What would you like to do? add edge 3 4 30
What would you like to do? add edge 1 4 100
What would you like to do? shortest 1
Distances from 1: 
Distance to 2: 10
Distance to 4: 60
Distance to 3: 30
Distance to 1: 0
```

## 6. Python program to implement the Bellman-Ford algorithm on a graph.

Problem Description
The problem is to find the shortest distance to all vertices from a source vertex in a weighted directed graph that can have negative edge weights. For the problem to be well-defined, there should be no cycles in the graph with a negative total weight.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function bellman-ford that takes a Graph object and a source vertex as arguments.
3. A dictionary distance is created with keys as the vertices in the graph and their value all set to infinity.
4. distance[source] is set to 0.
5. The algorithm proceeds by performing an update operation on each edge in the graph n – 1 times. Here n is the number of vertices in the graph.
6. The update operation on an edge from vertex i to vertex j is distance[j] = min(distance[j], distance[i] + weight(i, j)).
7. The dictionary distance is returned.

Program/Source Code
Here is the source code of a Python program to implement Bellman-Ford algorithm on a graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def bellman_ford(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object which can have negative edge weights.
    source is a Vertex object in g.
    """
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
 
    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))
 
    return distance
 
 
g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('bellman-ford <source vertex key>')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'bellman-ford':
        key = int(do[1])
        source = g.get_vertex(key)
        distance = bellman_ford(g, source)
        print('Distances from {}: '.format(key))
        for v in distance:
            print('Distance to {}: {}'.format(v.get_key(), distance[v]))
        print()
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To find all shortest distances from a source vertex, bellman-ford is called on the graph and the source vertex.



## Runtime Test Cases
```

Case 1:
Menu
add vertex <key>
add edge <src> <dest> <weight>
bellman-ford <source vertex key>
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add vertex 7
What would you like to do? add vertex 8
What would you like to do? add edge 1 2 10
What would you like to do? add edge 1 8 8
What would you like to do? add edge 2 6 2
What would you like to do? add edge 3 2 1
What would you like to do? add edge 3 4 1
What would you like to do? add edge 4 5 3
What would you like to do? add edge 5 6 -1
What would you like to do? add edge 6 3 -2
What would you like to do? add edge 7 2 -4
What would you like to do? add edge 7 6 -1
What would you like to do? add edge 8 7 1
What would you like to do? bellman-ford 1
Distances from 1: 
Distance to 5: 9
Distance to 6: 7
Distance to 7: 9
Distance to 2: 5
Distance to 1: 0
Distance to 8: 8
Distance to 3: 5
Distance to 4: 6
 
Case 2:
Menu
add vertex <key>
add edge <src> <dest> <weight>
bellman-ford <source vertex key>
display
quit
What would you like to do? add vertex 1
What would you like to do? bellman-ford 1
Distances from 1: 
Distance to 1: 0
 
What would you like to do? add vertex 2
What would you like to do? bellman-ford 1
Distances from 1: 
Distance to 1: 0
Distance to 2: inf
 
What would you like to do? add edge 1 2 2
What would you like to do? add vertex 3
What would you like to do? add edge 1 3 -1
What would you like to do? bellman-ford 1
Distances from 1: 
Distance to 1: 0
Distance to 3: -1
Distance to 2: 2
 
What would you like to do? add edge 3 2 2
What would you like to do? bellman-ford 1
Distances from 1: 
Distance to 1: 0
Distance to 3: -1
Distance to 2: 1
 
What would you like to do? quit
```


## 7. Python program to implement the Floyd-Warshall algorithm on a directed graph to find the shortest distance between all pairs of vertices.

Problem Description
The problem is to find the shortest distance between all pairs of vertices in a weighted directed graph that can have negative edge weights. For the problem to be well-defined, there should be no cycles in the graph with a negative total weight.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function floyd_warshall that takes a Graph object as argument.
3. A dictionary distance is created that can be indexed with two vertices and all the values set to infinity.
4. Another dictionary next_v is created that can be indexed with two vertices and all the values set to None.
5. The above is implemented by creating a dictionary with keys as the start vertices and values as another inner dictionary. This inner dictionary contains keys as the destination vertices and value as the the corresponding distance for each vertex pair.
6. distance[u][v] will contain the shortest distance from vertex u to v.
7. next_v[u][v] will be the next vertex after vertex v in the shortest path from u to v. It is None if there is no path between them. next_v[w][w] will be None for all w.
8. For all edges from v to n, distance[v][n] = weight(edge(v, n)) and next_v[v][n] = n.
9. For all vertices v, distance[v][v] = 0 and next_v[v][v] = None.
10. The algorithm then performs distance[v][w] = min(distance[v][w], distance[v][p] + distance[p][w]) for each possible pair v, w of vertices.
11. The above is repeated for each vertex p in the graph.
12. Whenever distance[v][w] is given a new minimum value, next_v[v][w] is updated to next_v[v][p].
13. The dictionaries distance and next_v are returned.
14. The function print_path is created to print the shortest path from one vertex to another vertex using the dictionary next_v.
15. Formally, the Floyd-Warshall algorithm defines W(k)[i][j] to refer to the shortest distance from i to j using only the vertices 1, …, k where i and j are not necessarily included.
16. For all edges (i, j), W(0)[i][j] = weight(edge(i, j)).
17. To find W(k)[i][j], note that in the shortest path from i to j, we can either have k or not have k included.
18. If k is not present, W(k)[i][j] = W(k – 1)[i][j].
19. If k is present, W(k)[i][j] = W(k – 1)[i][k] + W(k – 1)[k][j].
20. So we simply set W(k)[i][j] equal to the minimum of the above two values.
21. This program is an implementation of the Floyd-Warshall algorithm but uses only O(n^2) space instead of O(n^3) space which a straightforward implementation of the algorithm would take.

Program/Source Code
Here is the source code of a Python program to implement Floyd-Warshall algorithm on a graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def floyd_warshall(g):
    """Return dictionaries distance and next_v.
 
    distance[u][v] is the shortest distance from vertex u to v.
    next_v[u][v] is the next vertex after vertex v in the shortest path from u
    to v. It is None if there is no path between them. next_v[u][u] should be
    None for all u.
 
    g is a Graph object which can have negative edge weights.
    """
    distance = {v:dict.fromkeys(g, float('inf')) for v in g}
    next_v = {v:dict.fromkeys(g, None) for v in g}
 
    for v in g:
        for n in v.get_neighbours():
            distance[v][n] = v.get_weight(n)
            next_v[v][n] = n
 
    for v in g:
         distance[v][v] = 0
         next_v[v][v] = None
 
    for p in g: 
        for v in g:
            for w in g:
                if distance[v][w] > distance[v][p] + distance[p][w]:
                    distance[v][w] = distance[v][p] + distance[p][w]
                    next_v[v][w] = next_v[v][p]
 
    return distance, next_v
 
 
def print_path(next_v, u, v):
    """Print shortest path from vertex u to v.
 
    next_v is a dictionary where next_v[u][v] is the next vertex after vertex u
    in the shortest path from u to v. It is None if there is no path between
    them. next_v[u][u] should be None for all u.
 
    u and v are Vertex objects.
    """
    p = u
    while (next_v[p][v]):
        print('{} -> '.format(p.get_key()), end='')
        p = next_v[p][v]
    print('{} '.format(v.get_key()), end='')
 
 
g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('floyd-warshall')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'floyd-warshall':
        distance, next_v = floyd_warshall(g)
        print('Shortest distances:')
        for start in g:
            for end in g:
                if next_v[start][end]:
                    print('From {} to {}: '.format(start.get_key(),
                                                    end.get_key()),
                            end = '')
                    print_path(next_v, start, end)
                    print('(distance {})'.format(distance[start][end]))
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To find shortest distances between all pairs, floyd_warshall is called to get the dictionaries distance, next_v.
4. print_path is called on the dictionary next_v for each pair of vertices to print the paths and the dictionary distance is used to print the distance between each pair.


## Runtime Test Cases
```
Case 1:
Menu
add vertex <key>
add edge <src> <dest> <weight>
floyd-warshall
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add edge 1 2 3
What would you like to do? add edge 1 5 -4
What would you like to do? add edge 1 3 8
What would you like to do? add edge 2 5 7
What would you like to do? add edge 2 4 1
What would you like to do? add edge 3 2 4
What would you like to do? add edge 4 3 -5
What would you like to do? add edge 4 1 2
What would you like to do? add edge 5 4 6
What would you like to do? floyd-warshall
Shortest distances:
From 1 to 2: 1 -> 5 -> 4 -> 3 -> 2 (distance 1)
From 1 to 3: 1 -> 5 -> 4 -> 3 (distance -3)
From 1 to 4: 1 -> 5 -> 4 (distance 2)
From 1 to 5: 1 -> 5 (distance -4)
From 2 to 1: 2 -> 4 -> 1 (distance 3)
From 2 to 3: 2 -> 4 -> 3 (distance -4)
From 2 to 4: 2 -> 4 (distance 1)
From 2 to 5: 2 -> 4 -> 1 -> 5 (distance -1)
From 3 to 1: 3 -> 2 -> 4 -> 1 (distance 7)
From 3 to 2: 3 -> 2 (distance 4)
From 3 to 4: 3 -> 2 -> 4 (distance 5)
From 3 to 5: 3 -> 2 -> 4 -> 1 -> 5 (distance 3)
From 4 to 1: 4 -> 1 (distance 2)
From 4 to 2: 4 -> 3 -> 2 (distance -1)
From 4 to 3: 4 -> 3 (distance -5)
From 4 to 5: 4 -> 1 -> 5 (distance -2)
From 5 to 1: 5 -> 4 -> 1 (distance 8)
From 5 to 2: 5 -> 4 -> 3 -> 2 (distance 5)
From 5 to 3: 5 -> 4 -> 3 (distance 1)
From 5 to 4: 5 -> 4 (distance 6)
What would you like to do? quit
 
Case 2:
Menu
add vertex <key>
add edge <src> <dest> <weight>
floyd-warshall
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add edge 1 2 10
What would you like to do? add edge 2 3 -7
What would you like to do? add edge 1 3 5
What would you like to do? floyd-warshall
Shortest distances:
From 1 to 2: 1 -> 2 (distance 10)
From 1 to 3: 1 -> 2 -> 3 (distance 3)
From 2 to 3: 2 -> 3 (distance -7)
What would you like to do? quit
```
## 8. Python program to implement Johnson’s algorithm on a directed graph to find the shortest distance between all pairs of vertices.

Problem Description
The problem is to find the shortest distance between all pairs of vertices in a weighted directed graph that can have negative edge weights. For the problem to be well-defined, there should be no cycles in the graph with a negative total weight.

Problem Solution
1. Create classes for Graph and Vertex.
2. Create a function johnson that takes a Graph object g as argument.
3. It returns a dictionary distance where distance[u][v] is the minimum distance from vertex u to v.
4. The algorithm works by first adding a new vertex q to the graph g.
5. This vertex q is made to point to all other vertices wit zero-weight edges.
6. The Bellman-Ford algorithm is run on the graph with source vertex q to find the shortest distance from q to all other vertices. This is stored in bell_dist where bell_dist[v] is the shortest distance from q to v.
7. Modify the graph’s weight function and set it to w(u, v) = w(u, v) + bell_dist(u) – bell_dist(v).
8. Remove the vertex q from the graph.
9. Run Dijkstra’s algorithm on each source vertex in the graph to find the shortest distance from each source vertex to all other vertices in this modified graph.
10. These shortest distances are stored in distance where distance[u][v] is the shortest distance from u to v.
11. Add (bell_dist[v] – bell_dist[u]) to distance[u][v] for each pair of vertices u, v to get the shortest distances for the original graph.
12. Correct the weights in the graph by adding (bell_dist[v] – bell_dist[u]) to weight(u, v) for each edge (u, v) in the graph so that the graph is no longer modified.

Program/Source Code
Here is the source code of a Python program to implement Johnson’s algorithm on a directed graph. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def set_weight(self, dest, weight):
        """Set weight of edge from this vertex to dest."""
        self.points_to[dest] = weight
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def johnson(g):
    """Return distance where distance[u][v] is the min distance from u to v.
 
    distance[u][v] is the shortest distance from vertex u to v.
 
    g is a Graph object which can have negative edge weights.
    """
    # add new vertex q
    g.add_vertex('q')
    # let q point to all other vertices in g with zero-weight edges
    for v in g:
        g.add_edge('q', v.get_key(), 0)
 
    # compute shortest distance from vertex q to all other vertices
    bell_dist = bellman_ford(g, g.get_vertex('q'))
 
    # set weight(u, v) = weight(u, v) + bell_dist(u) - bell_dist(v) for each
    # edge (u, v)
    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[v] - bell_dist[n])
 
    # remove vertex q
    # This implementation of the graph stores edge (u, v) in Vertex object u
    # Since no other vertex points back to q, we do not need to worry about
    # removing edges pointing to q from other vertices.
    del g.vertices['q']
 
    # distance[u][v] will hold smallest distance from vertex u to v
    distance = {}
    # run dijkstra's algorithm on each source vertex
    for v in g:
        distance[v] = dijkstra(g, v)
 
    # correct distances
    for v in g:
        for w in g:
            distance[v][w] += bell_dist[w] - bell_dist[v]
 
    # correct weights in original graph
    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[n] - bell_dist[v])
 
    return distance
 
 
def bellman_ford(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object which can have negative edge weights.
    source is a Vertex object in g.
    """
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
 
    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))
 
    return distance
 
 
def dijkstra(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object.
    source is a Vertex object in g.
    """
    unvisited = set(g)
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
 
    while unvisited != set():
        # find vertex with minimum distance
        closest = min(unvisited, key=lambda v: distance[v])
 
        # mark as visited
        unvisited.remove(closest)
 
        # update distances
        for neighbour in closest.get_neighbours():
           if neighbour in unvisited:
               new_distance = distance[closest] + closest.get_weight(neighbour)
               if distance[neighbour] > new_distance:
                   distance[neighbour] = new_distance
 
    return distance
 
 
g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('johnson')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'johnson':
        distance = johnson(g)
        print('Shortest distances:')
        for start in g:
            for end in g:
                print('{} to {}'.format(start.get_key(), end.get_key()), end=' ')
                print('distance {}'.format(distance[start][end]))
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To find shortest distances between all pairs, johnson is called to get the dictionary distance.
4. The distances between each pair of vertices are then displayed.

## Runtime Test Cases
```

Case 1:
Menu
add vertex <key>
add edge <src> <dest> <weight>
johnson
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add edge 1 2 3
What would you like to do? add edge 1 3 8
What would you like to do? add edge 1 5 -4
What would you like to do? add edge 2 5 7
What would you like to do? add edge 2 4 1
What would you like to do? add edge 3 2 4
What would you like to do? add edge 4 3 -5
What would you like to do? add edge 4 1 2
What would you like to do? add edge 5 4 6
What would you like to do? johnson
Shortest distances:
1 to 1 distance 0
1 to 2 distance 1
1 to 3 distance -3
1 to 4 distance 2
1 to 5 distance -4
2 to 1 distance 3
2 to 2 distance 0
2 to 3 distance -4
2 to 4 distance 1
2 to 5 distance -1
3 to 1 distance 7
3 to 2 distance 4
3 to 3 distance 0
3 to 4 distance 5
3 to 5 distance 3
4 to 1 distance 2
4 to 2 distance -1
4 to 3 distance -5
4 to 4 distance 0
4 to 5 distance -2
5 to 1 distance 8
5 to 2 distance 5
5 to 3 distance 1
5 to 4 distance 6
5 to 5 distance 0
What would you like to do? quit
 
Case 2:
python 226__graph_johnson.py
Menu
add vertex <key>
add edge <src> <dest> <weight>
johnson
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? johnson
Shortest distances:
1 to 1 distance 0
1 to 2 distance inf
2 to 1 distance inf
2 to 2 distance 0
What would you like to do? add edge 1 2 100
What would you like to do? add vertex 3
What would you like to do? add edge 2 3 -50
What would you like to do? add edge 1 3 60
What would you like to do? johnson
Shortest distances:
1 to 1 distance 0
1 to 2 distance 100
1 to 3 distance 50
2 to 1 distance inf
2 to 2 distance 0
2 to 3 distance -50
3 to 1 distance inf
3 to 2 distance inf
3 to 3 distance 0
What would you like to do? quit
```
## 9. Python program to find if an undirected graph is bipartite using BFS.

Problem Description
The program creates a graph object and allows the user to determine whether the graph is bipartite.

Problem Solution
1. Create classes for Graph, Vertex and Queue.
2. Create a function is_bipartite that takes a Vertex object v and a set visited as arguments.
3. The function works by painting each vertex a colour opposite to the colour of its neighbours. If it is found not possible to do so, the graph is not bipartite.
4. The function begins by creating an empty set called visited and a Queue object, q.
5. It also creates a dictionary colour which maps each vertex to either 1 or 0 which represent two different colours. The Vertex object passed is mapped to 0.
6. It enqueues the passed Vertex object and also adds it to the set visited.
7. A while loop is created which runs as long as the queue is not empty.
8. In each iteration of the loop, the queue is dequeued and all of its neighbours are enqueued which have not already been visited.
9. In addition to enqueuing, they are also added to the set visited and the colour of each neighbour is set to the colour opposite to the colour of the dequeued element.
10. If a neighbour is found to be already visited and its colour is the same as that of the dequeued element, the graph is not bipartite and False is returned.
11. After the loop is finished, True is returned to indicate that the graph is bipartite.
12. Thus, the function returns True if the connected component containing v is bipartite. It also puts all nodes reachable from the source vertex in the set visited.

Program/Source Code
Here is the source code of a Python program to find if an undirected graph is bipartite using BFS. The program output is shown below.
```
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def add_undirected_edge(self, v1_key, v2_key, weight=1):
        """Add undirected edge (2 directed edges) between v1_key and v2_key with
        given weight."""
        self.add_edge(v1_key, v2_key, weight)
        self.add_edge(v2_key, v1_key, weight)
 
    def does_undirected_edge_exist(self, v1_key, v2_key):
        """Return True if there is an undirected edge between v1_key and v2_key."""
        return (self.does_edge_exist(v1_key, v2_key)
                and self.does_edge_exist(v1_key, v2_key))
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
def is_bipartite(vertex, visited):
    """Return True if component containing vertex is bipartite and put all
    vertices in its component in set visited."""
    colour = {vertex: 0}
    visited.add(vertex)
    q = Queue()
    q.enqueue(vertex)
    while not q.is_empty():
        current = q.dequeue()
 
        next_colour = 1 - colour[current] # switch colour
        for dest in current.get_neighbours():
            if dest not in visited:
                visited.add(dest)
                colour[dest] = next_colour
                q.enqueue(dest)
            else:
                if colour[dest] != next_colour:
                    return False
    return True
 
 
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <vertex1> <vertex2>')
print('bipartite')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            v1 = int(do[2])
            v2 = int(do[3])
            if v1 not in g:
                print('Vertex {} does not exist.'.format(v1))
            elif v2 not in g:
                print('Vertex {} does not exist.'.format(v2))
            else:
                if not g.does_undirected_edge_exist(v1, v2):
                    g.add_undirected_edge(v1, v2)
                else:
                    print('Edge already exists.')
 
    elif operation == 'bipartite':
        bipartite = True
        visited = set()
        for v in g:
            if v not in visited:
                if not is_bipartite(v, visited):
                    bipartite = False
                    break
 
        if bipartite:
            print('Graph is bipartite.')
        else:
            print('Graph is not bipartite.')
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break
 ```
Program Explanation
1. An instance of Graph is created.
2. A menu is presented to the user to perform various operations on the graph.
3. To determine whether the graph is bipartite, is_bipartite is called with a vertex from the graph and an empty set visited.
4. If is_bipartite returns True, the graph is not bipartite. Otherwise, if not all vertices were visited, is_bipartite is called again with an unvisited source vertex.
5. This continues until all vertices have been visited or is_bipartite returns False.
6. If all vertices have been visited, the graph is bipartite.

```
Runtime Test Cases
Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <vertex1> <vertex2>
bipartite
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add vertex 7
What would you like to do? add edge 1 2
What would you like to do? add edge 2 3
What would you like to do? add edge 3 4
What would you like to do? add edge 5 6
What would you like to do? add edge 6 7
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 7 1
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 6 1
What would you like to do? bipartite
Graph is not bipartite.
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <vertex1> <vertex2>
bipartite
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 1 2
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 3 4
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 1 4
What would you like to do? bipartite
Graph is bipartite.
What would you like to do? add edge 2 4
What would you like to do? bipartite
Graph is not bipartite.
What would you like to do? quit
```
