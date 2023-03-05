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

