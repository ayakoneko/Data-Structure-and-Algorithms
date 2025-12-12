## Navigation System 
# Edges: roads (w distance), Nodes: intersections (w toll costs)
# with Dijkstra’s Algorithm 

# 1. shortest route (minimize distance)
# 2. most cost-effective route (minimize toll fees)
# 3. balanced route (consider both distance and toll fees)

#input
map = {
    "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
    "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
    "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
    "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
    "E": {"toll": 5, "roads": {"C": 6, "D": 2}},
}


def Dijkstra(map, start, end, method):
    visited=set()
    point={node: float("inf") for node in map}
    point[start]=0
    previous_nodes={}

    while len(visited) < len(map):
        current_node=None
        current_min_point=float("inf")

        for node in map:
            if node not in visited and point[node] < current_min_point:
                current_node=node
                current_min_point=point[node]
            
        if current_node is None: # point[node] stay "inf" if path is not connected, once all connected node is visited, it will return to disconeccted node (never process in for loop as second condition never meet)
            break #exit the loop

        visited.add(current_node)

        for neighbor, distance in map[current_node]["roads"].items():
            if neighbor in visited:
                continue #skip and continue
            
            toll=map[neighbor]["toll"]

            new_point=method(point[current_node], distance, toll)
            if new_point < point[neighbor]:
                point[neighbor]=new_point
                previous_nodes[neighbor]=current_node


    # reconstruct path 
    path=[]
    node=end
    while node in previous_nodes:
        path.insert(0, node) #add in front of path list
        node=previous_nodes[node]
    if node == start:
        path.insert(0, start) #stop the next while loop as A(start node) is not in previous_nodes
    else:
        return None, float("inf") #if node never reach to start, it means that there is no valid path and destination is uncreachable
    
    path_str= ' -> '.join(path)

    return path_str, point[end]

#path strategies (method)
def shortest(current_point, distance, toll):
    return current_point + distance   
        
def cheapest(current_point, distance, toll):
    return current_point + toll
        
def balanced(current_point, distance, toll):
    return current_point + distance + toll


start=input("Start: ")
end=input("End: ")

shortest_path, shortest_distance=Dijkstra(map, start, end, shortest)
cheapest_path, cheapest_distance=Dijkstra(map, start, end, cheapest)
balanced_path, balanced_distance=Dijkstra(map, start, end, balanced)

print(f"shortest   path: {shortest_path:<20} distance: {shortest_distance:<10}")
print(f"cheapest   path: {cheapest_path:<20} toll: {cheapest_distance:<10}")
print(f"balanced   path: {balanced_path:<20} cost: {balanced_distance:<10}")





# strategy_path, strategy_distance=Dijkstra(map, start, end, strategylist[strategy])
# print ("Result: ", strategy_path, strategy_distance)

# strategylist = {"shortest":shortest, "cheapest":cheapest, "balanaced":balanced}
# strategy=input("Choose path strategy from shortest/cheapest/balanced: ")      





# from queue import Queue

# class Navigation:
#     def __init__(self):
#         self.roads={} #node: list of neighbour and distance
#         self.tolls={} #node: toll fee
    
#     def add_intersection (self, node, toll=0):
#         self.roads[node]=[]
#         self.tolls[node]=toll

#     def add_road(self, node1, node2, distance):
#         self.roads[node1].append((node2, distance)) #for node1(left end), add node2(right end) and distance between them
#         self.roads[node2].append((node1, distance)) #for node2(right end), add node1(left end) and distance between them

#     def PrirityQueue(self, start, destination, route_type="distance", alpha=1.0, distance_limit=100, toll_limit=100):
#         PQ=Queue()
#         PQ.put((0, 0, self.tolls[start], [start])) #(priority/cost, distance, toll, path)
#         best_route=None
#         best_cost=float("inf")
        
#         while not PQ.empty():
#             cost, dist_sum, toll_sum, path=PQ.get()
#             node=path[-1]

#             if node==destination: #when node reaches to destination, check if it exceed distance and toll limits 
#                 if dist_sum>distance_limit and toll_sum>toll_limit:
#                     continue
#                 if cost<best_cost:
#                     best_cost=cost
#                     best_route={
#                         "total_distance": dist_sum,
#                         "total_toll": toll_sum,
#                         "path": path
#                     }
#                 continue
            
#             for neighbor, road_dist in self.roads[node]:
#                 if neighbor in path: #avoide cycle route
#                     continue
            
#                 new_dist=dist_sum+road_dist
#                 new_toll=toll_sum+self.tolls[neighbor]

#                 #route options
#                 if route_type=="distance":
#                     priority=new_dist
#                 elif route_type=="toll":
#                     priority=new_toll
#                 elif route_type=="balanced":
#                     priority=new_dist+alpha*new_toll
#                 else:
#                     continue

#                 PQ.put((priority, new_dist, new_toll, path+[neighbor]))

#         return best_route

#     def routefinder(self, start, destiination, alpha=1.0):
#         return {
#             "shortest_route": self.PrirityQueue(start, destiination, "distance"),
#             "cheapest_route": self.PrirityQueue(start, destiination, "toll"),
#             "best_balanced_route": self.PrirityQueue(start, destiination, "balanced", alpha=alpha),
#         }

# Map=Navigation()

# for node, toll in [("A", 0), ("B", 2), ("C", 3), ("D", 2), ("E", 5)]:
#     Map.add_intersection(node, toll)

# Map.add_road("A", "B", 4)
# Map.add_road("A", "C", 8)
# Map.add_road("B", "C", 2)
# Map.add_road("B", "D", 5)
# Map.add_road("C", "D", 3)
# Map.add_road("C", "E", 6)
# Map.add_road("D", "E", 2)

# routes=Map.routefinder("A", "E", alpha=2.0)

# print(routes)

# 1. shortest route (minimize distance)
# 2. most cost-effective route (minimize toll fees)
# 3. balanced route (consider both distance and toll fees)

# Map = {
#     "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
#     "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
#     "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
#     "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
#     "E": {"toll": 5, "roads": {"C": 6, "D": 2}},
# }




