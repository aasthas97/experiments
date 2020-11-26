"""Iterative breadth-first and depth-first traversal of directed graph.
Each node of the graph represents a course. An edge from course A to course B indicates that A is a sufficient pre-requisite for B.
Using two graph traversal algorithms, this script finds a path from any given course to 'Brain Computer Interfacing'."""

class Graph:
    def __init__(self, v_list =None):
        self.gdict = {}
        if v_list is not None:
            for vertex in v_list:
                self.addVertex(vertex)

    def addVertex(self, vertex):
        self.gdict[vertex] = []

    def addEdge(self, start, end):
        if start not in self.gdict.keys():
            print("Start vertex not found : ", start)
        if type(end) == list:
            for vertex in end:
                self.addEdge(start, vertex)
        elif end not in self.gdict.keys():
            print("End vertex not found : ", end)
        else:
            self.gdict[start].append(end)

    def getVertices(self):
        return self.gdict.keys()

    def getNeighbours(self, vertex):
        if vertex in self.gdict.keys():
            return self.gdict[vertex]
        else:
            print("Vertex not found.")
    
    def bfs(self, source, g):
        """BFS traversal to find shortest path between source and target
        Input params: source - Start node
        g - target node
        Returns path list or None (if no path)"""
        if source not in self.getVertices():
            print('Source node invalid.')
            return
        
        travel = {}
        queue = []
        visited = []
        queue.append(source)
        while queue:
            s = queue.pop(0) 
            visited.append(s)
            child_nodes = self.getNeighbours(s)

            for node in child_nodes:
                if node == g:
                    print('Found goal')
                    travel[node] = s # store visited node information in child: parent format
                    path = self.printPath(travel, source, node)
                    return path
                else:
                    if node not in visited:
                        travel[node] = s # store visited node information in child: parent format
                        queue.append(node)
    
    def printPath(self, travelhistory, source, target):
        '''Travel history: Dictionary containing details of all visited nodes in node: parent node format'''
        temp = []
        child = target
        parent = travelhistory[child]
        while parent != source:
            temp.append(child)
            child = parent
            parent = travelhistory[child]
        temp.append(source)
        temp.reverse()
        
        return temp
        
                        
    def wrapper_fn(self, start, target): #wrapper function calls DFS and stores path
        path = []
        def dfs(graph, start, target, visited=[]): # recursive DFS
            visited.append(start)
            if start == target:
                return
            child_nodes = [child for child in graph.getNeighbours(start) if child not in visited]
            for node in child_nodes:
                if node==target:
                    path.append(node)
                    path.append(start)
                    visited.append(node)
                    break
                dfs(graph, node, target, visited)
                if target in visited:
                    path.append(start)
                    break
            return visited
        dfs(self, start, target)
        path = path[::-1] if path else "Path does not exist"
        return path

courses = ["Biology", "Physics", "Chemistry", "Computer Science", "Cognitive Psychology", "Psychology", "Cognitive Neuroscience", "Anatomy", "Neurobiology", "Neuroscience", 
           "Logic and Cognitive Science", "Social Psychology", "Game Design", "Lego Robotics", "Robotics", "Mechanics", "Neural Interfacing", "Cognitive Science", 
           "Computational Tools in Cognitive Science", "Philosophy of Mind", "Anthropology", "Linguistics", "Machine Learning", "Artificial Intelligence", 
           "Natural Language Processing", "Embodied Cognition", "Electronics",  "Haptic Systems", "Signal Processing", "Embedded Systems", "Brain Computer Interfacing"]
  
course_graph = Graph(courses)

course_graph.addEdge("Biology", ["Anatomy", "Neurobiology", "Neuroscience","Cognitive Science"])
course_graph.addEdge("Physics", ["Mechanics", "Electronics", "Cognitive Science", "Game Design"])
course_graph.addEdge("Chemistry", ["Neurobiology", "Neuroscience", "Cognitive Science"])
course_graph.addEdge("Linguistics", ["Anthropology","Artificial Intelligence", "Natural Language Processing", "Cognitive Science"])
course_graph.addEdge("Computer Science", ["Cognitive Science", "Computational Tools in Cognitive Science", "Artificial Intelligence", "Game Design"])
course_graph.addEdge("Psychology", ["Cognitive Psychology", "Social Psychology", "Anthropology", "Cognitive Science"])
course_graph.addEdge("Mechanics", ["Lego Robotics", "Robotics", "Electronics", "Cognitive Science", "Embedded Systems"])
course_graph.addEdge("Electronics", ["Mechanics", "Embedded Systems", "Lego Robotics", "Robotics", "Signal Processing", "Haptic Systems", "Cognitive Science"])
course_graph.addEdge("Cognitive Science", ["Cognitive Psychology", "Neurobiology", "Cognitive Neuroscience", "Logic and Cognitive Science","Cognitive Science", "Linguistics", "Computational Tools in Cognitive Science", "Philosophy of Mind", "Anthropology", "Embodied Cognition"])
course_graph.addEdge("Cognitive Psychology", ["Social Psychology", "Anthropology", "Artificial Intelligence"])
course_graph.addEdge("Philosophy of Mind", ["Anthropology", "Artificial Intelligence"])
course_graph.addEdge("Neurobiology", ["Neuroscience", "Neural Interfacing"])
course_graph.addEdge("Anatomy", ["Neurobiology", "Haptic Systems", "Embodied Cognition"])
course_graph.addEdge("Computational Tools in Cognitive Science", ["Artificial Intelligence", "Embedded Systems", "Game Design"])
course_graph.addEdge("Logic and Cognitive Science", ["Artificial Intelligence", "Signal Processing", "Game Design"])
course_graph.addEdge("Artificial Intelligence", ["Machine Learning", "Natural Language Processing","Game Design", "Embodied Cognition"])
course_graph.addEdge("Machine Learning", ["Lego Robotics", "Robotics", "Natural Language Processing"])
course_graph.addEdge("Game Design", ["Lego Robotics", "Haptic Systems"])
course_graph.addEdge("Lego Robotics", ["Robotics", "Signal Processing", "Embedded Systems"])
course_graph.addEdge("Robotics", ["Haptic Systems", "Signal Processing", "Embedded Systems"])
course_graph.addEdge("Signal Processing", ["Neural Interfacing", "Embedded Systems"])
course_graph.addEdge("Embedded Systems", ["Robotics"])
course_graph.addEdge("Neuroscience", ["Neural Interfacing",  "Brain Computer Interfacing"])
course_graph.addEdge("Haptic Systems", ["Signal Processing"])
course_graph.addEdge("Neural Interfacing", ["Haptic Systems", "Signal Processing", "Embedded Systems", "Brain Computer Interfacing"])

# Uncomment for DFS traversal. To change goal course, change target_node
# source_node = input("Enter the course to be used as the start node : ")
# target_node = 'Brain Computer Interfacing'
# path = course_graph.wrapper_fn(source_node, target_node)
# if path == 'Path does not exist':
#     print(path)
# else:
#     print(' --> '.join(path))

# Uncomment for BFS traversal. To change goal course, change target_node
# source_node = input("Enter the course to be used as the start node : ")
# target_node = 'Brain Computer Interfacing'
# path = course_graph.bfs(source_node, g = target_node)
# if path == None:
#     print('Path does not exist')
# else:
#     print(' --> '.join(path))
