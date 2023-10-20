#NOTE: This is NOT my program. This program is taken from
#https://www.educative.io/answers/how-to-implement-a-graph-in-python
#I have just cleaned up + added data, in order to understand graph
#traversal within Python.

#need to change terminology of variables so that the two programs match.
#vertices = nodes
#vertex = node
#need to change syntax of functions vs variables:
#variables = this_is_var
#functions = thisIsFunc

# Add a vertex to the set of vertices and the graph
def add_vertex(v):
    
  global graph
  global vertices_no
  global vertices
  
  if v in vertices:
    print("Vertex ", v, " already exists")
    
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
            
    temp = []
    
    for i in range(vertices_no):
        temp.append(0)
        
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    
    global graph
    global vertices_no
    global vertices
    
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
        
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
        
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
    
  global graph
  global vertices_no
  
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " Edge weight: ", graph[i][j])
     
# stores the vertices in the graph
vertices = []

# stores the number of vertices in the graph
vertices_no = 0
graph = []

# Add vertices to the graph
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_vertex('F')

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge('A', 'B', 11)
add_edge('A', 'C', 16)
add_edge('B', 'C', 14)
add_edge('B', 'D', 18)
add_edge('C', 'D', 10)
add_edge('C', 'E', 17)
add_edge('D', 'E', 15)
add_edge('D', 'F', 12)
add_edge('E', 'F', 16)

#print_graph()
#for k in graph:
    #print(k)