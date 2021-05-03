#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 2021

@author: maksym
"""

# def recurs(node, cost, number, visited_nodes):
#     if number == string_len:
#         if cost < answer_cost:
#             answer_cost = cost
#         return
            
#     if cost < answer_cost:
#         for edge in node.edges_from:
#             if (edge.to_node not in visited_nodes):
#                 if (edge.to_node.letter == s[number]):
#                     visited_nodes = []
#                     number += 1
#                 visited_nodes.append(node)
#                 recurs(edge.to_node, cost + edge.weight, number, visited_nodes)
            

class Edge():
    
    def __init__(self, to_node, weight):
        self.to_node = to_node
        self.weight = weight

class Node():
    
    def __init__(self, letter, edges_from, index):
        self.letter = letter
        self.edges_from = edges_from
        self.index = index
        
    def Add_edge_from(self, weight, to_node):
        self.edges_from.append(Edge(to_node, weight))
        
        
class Graph():
    
    def __init__(self, Nodes):
        self.nodes = Nodes
    
    def add_node(self, node):
        self.nodes.append(node)
        
    # def _get_cost_to_letter(self, _from_node, letter, curr_cost, visited_nodes):
    #     # print("!!!!!!!_get_cost_to_letter!!!!! {0} -> {1} curcost: {2} visited {3}".format(_from_node.letter, letter, curr_cost, len(visited_nodes)))
    #     print("s", _from_node.letter, "-")
    #     for edge in _from_node.edges_from:
    #         # print("letter: {0}, _frome_node.letter: {1} curr edge letter: {2} weight: {3} ".format(letter, _from_node.letter, edge.to_node.letter, edge.weight))
    #         print("-",edge.weight,"-", edge.to_node.letter)
    #         if edge.to_node.letter == letter \
    #             and ((self.min_cost == -1) or (self.min_cost >= curr_cost + edge.weight)):
                 
    #             # print("edge.to_node.letter == letter")
    #             print("-",letter,"!!!", curr_cost + edge.weight)
                
    #             if self.min_cost == curr_cost + edge.weight:
    #                 self.dest_node.append(edge.to_node)
    #             else:
    #                 self.dest_node = [edge.to_node]
                    
    #             self.min_cost = curr_cost + edge.weight
                

                    
    #         if (curr_cost + edge.weight < self.min_cost or self.min_cost == -1) \
    #             and (edge.to_node not in visited_nodes):
                    
    #             # print("edge.to_node.letter({0}) != letter({1})".format(edge.to_node.letter, letter))
    #             print("-x-")
    #             visited_nodes.append(_from_node)
    #             self._get_cost_to_letter(edge.to_node, letter, \
    #                                       curr_cost + edge.weight, visited_nodes)
    #             # print("end of edge.to_node.letter({0}) != letter({1})".format(edge.to_node.letter, letter))
    #             print("///")
    #     return   

    # def get_min_cost_to_letter(self, from_nodes, letter):
    #     self.min_cost = -1
    #     self.dest_node = []
        
    #     for from_node in from_nodes:
    #         if letter == from_node.letter: #!!!!!!!!!!!!!!!!!!!!!!
    #             return 0, from_node
            
    #         self._get_cost_to_letter(from_node, letter, 0, [])
        
    #     return self.min_cost, self.dest_node              
  
    def dijkstra(self, node):
        # Получает индекс узла (или поддерживает передачу int)
        nodenum = node.index
        # Заставляет массив отслеживать расстояние от одного до любого узла
        # в self.nodes. Инициализирует до бесконечности для всех узлов, кроме 
        # начального узла
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = float("inf")
        
        dist[nodenum] = 0
        # Добавляет в очередь все узлы графа
        # Отмечает целые числа в очереди, соответствующие индексам узла
        # локаций в массиве self.nodes 
        queue = [i for i in range(len(self.nodes))]
        # Набор увиденных на данный момент номеров 
        seen = set()
        while len(queue) > 0:
            # Получает узел в очереди, который еще не был рассмотрен
            # и который находится на кратчайшем расстоянии от источника
            min_dist = float("inf")
            min_node = None
            for n in queue: 
                if dist[n] < min_dist and n not in seen:
                    min_dist = dist[n]
                    min_node = n
            
            # Добавляет мин. расстояние узла до увиденного, убирает очередь
            if min_node == None:
                return dist
            
            queue.remove(min_node)
            seen.add(min_node)
            # Получает все следующие перескоки
            #connections = self.connections_from(min_node)
            connections = self.nodes[min_node].edges_from
            # Для каждой связи обновляет путь и полное расстояние от  
            # исходного узла, если полное расстояние меньше
            # чем текущее расстояние в массиве dist
            #for (node, weight) in connections: 
            for edge in connections: 
                tot_dist = edge.weight + min_dist
                if tot_dist < dist[edge.to_node.index]:
                    dist[edge.to_node.index] = tot_dist

        return dist

          
def only_dist_to_letter(graph, dist, letter):
    new_dist = []
    for i in range(len(dist)):
        if graph.nodes[i].letter == letter:
            new_dist.append(dist[i])
    return new_dist

def Get_node_connections(node, visited):
    for edge in node.edges:
        if edge.to_node not in visited:
            visited.append(edge.to_node)
            visited.append(Get_node_connections(edge.to_node, visited))
    return visited


def Get_connected_graphs(graph):
    graphs = []
    not_visited = graph.nodes
    curr_graph = Graph([])
    
    while len(not_visited) > 0:
        node = not_visited[0]
        nodes = node.get_connections()
        for node in nodes:
            not_visited.remove(node)
            curr_graph.add_node(node)
            
        graphs.append(curr_graph)
            

Test_count = int(input())

for tc in range(Test_count):
    
    # pppp = input()

    graph = Graph([])    
    
    node_count, edge_count, string_len = map(int, input().split())
    
    s = input()
    
    i = 0
    for letter in map(str, input().split()):
        graph.add_node(Node(letter, [], i))
        i += 1
        
    for i in range(edge_count):
        node_num0, node_num1, weight = map(int, input().split())
        graph.nodes[node_num0 - 1].Add_edge_from(weight, graph.nodes[node_num1 - 1])
        graph.nodes[node_num1 - 1].Add_edge_from(weight, graph.nodes[node_num0 - 1])
        # print("added {0} <-> {1} ({2} <-> {3}) weight: {4}".format(node_num0 - 1, node_num1 - 1, \
        #     graph.nodes[node_num0 - 1].letter, graph.nodes[node_num1 - 1].letter, weight))
     
    # graphs = Get_connected_graphs(graph, [])
        
    # total_length = 0
    # curr_point = []
    # answer_cost = 0
    # cost0 = -1
    
    # for node in graph.nodes: #find 1 nodes
        
    #     if node.letter == s[0]:
    #         curr_point.append(node)
        
        
    # if curr_point == []:
    #     print(-1)
        
    # else:
    #     for l in s[1:]:
    #         cost, curr_point = graph.get_min_cost_to_letter(curr_point, l)
            
    #         if cost == -1:
    #             answer_cost = -1
    #             break
    #         else:
    #             answer_cost += cost
    
    #     # cost = 0
        
    #     # for node in graph.nodes:
    #     #     if node.letter == s[0]:
    #     #         recurs(node, 0, 1, [])
            
        
            
    #     print(answer_cost)
    
    curr_points = []
    for node in graph.nodes: #find 1 nodes
        
        if node.letter == s[0]:
            curr_points.append([node, 0]) # node, cost to reach
            
    for letter in s[1:]:
    # получаем минимальные расстояния до всех вершин с текущей буквой
        # расстояния от первой вершины с прошлой буквой    
        dist = graph.dijkstra(curr_points[0][0])
        dist = only_dist_to_letter(graph, dist, letter)
        cost = curr_points[0][1]
        for i in range(len(dist)):
            dist[i] += cost
            
        # обновляем для остальных если расстояние меньше
        for i in range(1, len(curr_points)):
            new_dist = graph.dijkstra(curr_points[i][0])
            new_dist = only_dist_to_letter(graph, new_dist, letter)
            new_cost = curr_points[i][1]
            
            for j in range(len(new_dist)):
                
                if new_dist[j] + new_cost < dist[j]:
                    dist[j] = new_dist[j] + new_cost
        # На данном этапе имеем массив с кратчайшими расстояниями до всех букв letter            
        # print(dist)
        curr_points = []
        for node in graph.nodes: #find new nodes
            if node.letter == letter:
                curr_points.append([node, dist.pop(0)]) # node, cost to reach
        
        if curr_points == []:
            curr_points = [-1, -1]
            break
        
    
    min_dist = -1
    for i in curr_points:
        if i[1] < min_dist or min_dist == -1:
            min_dist = i[1]
            
    if min_dist == float("inf"):
        print(-1)
    else:
        print(min_dist)
            
        





