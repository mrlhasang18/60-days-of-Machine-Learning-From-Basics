'''
Defination:
 - Graph is an collection of nodes connected by edges.It is also recrusive DS.
 - Graphs has two parts entity  = node and the link that connects the nodes are edges.
 - example: google maps, facebook friend suggestion, flight routes, internet, etc.
 
Difference between Tree and graph:
 - In Tree there should only be one path between the 2 nodes.Tree can be thought of special type of graph.
 
There are 2 types of graph:
1. Directed Graph
2. Undirected Graph
3. Weighted graph   : edges if the graph are weighted

'''

# code implementation: 

# node creation:

class graph:
    
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict ={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    def print(self):
        print("Graph dict = {")
        for key, value in self.graph_dict.items():
            print(f"  {key}:{value},")
        print("}")
    
    # get paths between nodes
    def get_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self, start,end, path=[]):
        path = path + [start]
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                a = self.get_shortest_path(node, end, path)
                if shortest_path is None or len(a) < len(shortest_path):
                    shortest_path = a
        
        return shortest_path

if __name__ == '__main__':
    
    print(" \n----------- Graphs in routes location ---------\n")
    # tuple: immutable
    
    loc = [
        ('makwanpur','kathmandu'),
        ('kathmandu','lalitpur'),
        ('kathmandu','bhaktapur'),
        ('bhaktapur','kathmandu'),
        ('bhaktapur','lalitpur'),
        ('lalitpur','kathmandu'),
        ('lalitpur','bhaktapur')
    ]
    
    route = graph(loc)
    route.print()
    start  = "makwanpur"
    end = "bhaktapur"
    print(f"\nPath from {start} to {end} are : \n",route.get_path(start,end))
    
    print(f"\nShortest path from {start} to {end} is : ",route.get_shortest_path(start,end))
    
    start = 'bhaktapur'
    end =  'kathmandu'
    
    print(f"\nPath from {start} to {end} are : \n",route.get_path(start,end))
    
    print(f"\nShortest path from {start} to {end} is : ",route.get_shortest_path(start,end))