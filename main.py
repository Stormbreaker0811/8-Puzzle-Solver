from queue import *
class main:
    def __init__(self,initial_state):
        self.initial_state = initial_state
        self.goal_state = [1,2,3,4,5,6,7,8,0]
        self.visited = []
        self.queue = Queue()
        self.path = []
        self.path_cost = 0
        self.max_queue_size = 0
        self.nodes_expanded = 0
        self.depth = 0
        self.max_depth = 0
        self.solution = False
        self.algorithm = ""
        self.heuristic = ""
        self.heuristic_cost = 0
        self.heuristic_cost_list = []
        self.heuristic_cost_list.append(self.heuristic_cost)
    def bfs_solver(self):
        self.queue.put(self.initial_state)
        self.visited.append(self.initial_state)
        while not self.queue.empty():
            self.max_queue_size = max(self.max_queue_size, self.queue.qsize())
            self.nodes_expanded += 1
            current_state = self.queue.get()
            print(current_state)
            self.path.append(current_state)
            if current_state == self.goal_state:
                self.solution = True
                break
            else:
                self.depth += 1
                self.max_depth = max(self.max_depth, self.depth)
                self.get_children(current_state)
                self.depth -= 1
        if self.solution:
            print("Solution found")
            print("Path: ", self.path)
            print("Path cost: ", self.path_cost)
            print("Max queue size: ", self.max_queue_size)
            print("Nodes expanded: ", self.nodes_expanded)
            print("Max depth: ", self.max_depth)
        else:
            print("Solution not found")
    def get_children(self, current_state):
        index = current_state.index(0)
        if index == 0:
            self.move_right(current_state)
            self.move_down(current_state)
        elif index == 1:
            self.move_left(current_state)
            self.move_right(current_state)
            self.move_down(current_state)
        elif index == 2:
            self.move_left(current_state)
            self.move_down(current_state)
        elif index == 3:
            self.move_right(current_state)
            self.move_up(current_state)
            self.move_down(current_state)
        elif index == 4:
            self.move_left(current_state)
            self.move_right(current_state)
            self.move_up(current_state)
            self.move_down(current_state)
        elif index == 5:
            self.move_left(current_state)
            self.move_up(current_state)
            self.move_down(current_state)
        elif index == 6:
            self.move_right(current_state)
            self.move_up(current_state)
        elif index == 7:
            self.move_left(current_state)
            self.move_right(current_state)
            self.move_up(current_state)
        elif index == 8:
            self.move_left(current_state)
            self.move_up(current_state)
    def move_left(self, current_state):
        print("Left")
        index = current_state.index(0)
        if index not in [0, 3, 6]:
            new_state = current_state.copy()
            new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_right(self, current_state):
        print("Right")
        index = current_state.index(0)
        if index not in [2, 5, 8]:
            new_state = current_state.copy()
            new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_up(self, current_state):
        print("Up")
        index = current_state.index(0)
        if index not in [0, 1, 2]:
            new_state = current_state.copy()
            new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_down(self, current_state):
        print("Down")
        index = current_state.index(0)
        if index not in [6, 7, 8]:
            new_state = current_state.copy()
            new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def astar_solver(self):
        print("In A*")
        self.queue = Queue()
        self.visited = []
        self.path = []
        self.path_cost = 0
        self.nodes_expanded = 0
        self.max_queue_size = 0
        self.max_depth = 0
        self.depth = 0
        self.solution = False
        self.heuristic_cost_list = []
        self.queue.put(self.initial_state)
        self.visited.append(self.initial_state)
        while not self.queue.empty():
            self.max_queue_size = max(self.max_queue_size, self.queue.qsize())
            self.nodes_expanded += 1
            current_state = self.queue.get()
            print(current_state)
            self.path.append(current_state)
            if current_state == self.goal_state:
                self.solution = True
                break
            else:
                self.depth += 1
                self.max_depth = max(self.max_depth, self.depth)
                self.get_children_astar(current_state)
                self.depth -= 1
        if self.solution:
            print("Solution found")
            print("Path: ", self.path)
            print("Path cost: ", self.path_cost)
            print("Max queue size: ", self.max_queue_size)
            print("Nodes expanded: ", self.nodes_expanded)
            print("Max depth: ", self.max_depth)
        else:
            print("Solution not found")
    def get_children_astar(self, current_state):
        index = current_state.index(0)
        if index == 0:
            self.move_right_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 1:
            self.move_left_astar(current_state)
            self.move_right_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 2:
            self.move_left_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 3:
            self.move_right_astar(current_state)
            self.move_up_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 4:
            self.move_left_astar(current_state)
            self.move_right_astar(current_state)
            self.move_up_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 5:
            self.move_left_astar(current_state)
            self.move_up_astar(current_state)
            self.move_down_astar(current_state)
        elif index == 6:
            self.move_right_astar(current_state)
            self.move_up_astar(current_state)
        elif index == 7:
            self.move_left_astar(current_state)
            self.move_right_astar(current_state)
            self.move_up_astar(current_state)
        elif index == 8:
            self.move_left_astar(current_state)
            self.move_up_astar(current_state)
    def move_left_astar(self, current_state):
        print("Left")
        index = current_state.index(0)
        if index not in [0, 3, 6]:
            new_state = current_state.copy()
            new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_right_astar(self, current_state):
        print("Right")
        index = current_state.index(0)
        if index not in [2, 5, 8]:
            new_state = current_state.copy()
            new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_up_astar(self, current_state):
        print("Up")
        index = current_state.index(0)
        if index not in [0, 1, 2]:
            new_state = current_state.copy()
            new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def move_down_astar(self, current_state):
        print("Down")
        index = current_state.index(0)
        if index not in [6, 7, 8]:
            new_state = current_state.copy()
            new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
            if new_state not in self.visited:
                self.queue.put(new_state)
                self.visited.append(new_state)
                self.path_cost += 1
    def get_heuristic(self, current_state):
        heuristic = 0
        for i in range(9):
            if current_state[i] != self.goal_state[i]:
                heuristic += 1
        return heuristic