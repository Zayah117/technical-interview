# QUESTION 1

def question1(s, t):
    # if t is larger than s return false
    if len(t) > len(s):
        return False

    
    for i in range(len(s) - len(t) + 1):
        if sorted(s[i:i+len(t)]) == sorted(t):
            return True
        
    return False

# print question1("udacity", "adciuy")



# QUESTION 2

def is_palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

def question2(a):
    for num_of_letters in range(len(a)):
        for i in range(num_of_letters + 1):
            test_case = a[i:len(a)-num_of_letters+i]
            if is_palindrome(test_case):
                return test_case
            
    return None

# print question2("racecar")



# QUESTION 3
def question3(G):
    # Get vertices from G
    try:
        vertices = sorted(G.keys())
    except AttributeError:
        return None

    # Setup dictionary S
    S = {}
    S[vertices[0]] = []

    # Add vertices to S until it's as big as G
    while len(S) < len(G):
        short_con = None
        for vertex in S:
            new_con = get_short_edge(vertex, get_reverse_graph(G, S, vertices))
            # print "--" + str(short_con)
            # print new_con
            if new_con[0] and new_con[1]:
                if not short_con or short_con[1][1] > new_con[1][1]:
                    short_vert = vertex
                    short_con = new_con
        # print short_con
        
        S[short_vert].append((short_con[0], short_con[1][1]))
        S[short_con[0]] = [short_con[1]]

    return S

def get_short_edge(comp_vertex, G):
    # print "CALLING FUNCTION ON " + str(comp_vertex)
    short_edge = None
    short_vertex = None
    for vertex in G:
        # print vertex
        for connected_edge in G[vertex]:
            # print connected_edge
            if connected_edge[0] == comp_vertex:
                # print "^connected"
                if not short_edge or short_edge[1] > connected_edge[1]:
                    # print "^new short"
                    short_edge = connected_edge
                    short_vertex = vertex
             
    return short_vertex, short_edge

def get_reverse_graph(G, S, vertices):
    G_minus_S = {}
    
    for i in range(len(vertices)):    
        if vertices[i] in G and vertices[i] not in S:
            G_minus_S[vertices[i]] = G[vertices[i]]

    return G_minus_S
        

graph1 = {'A': [('B', 1), ('C', 1), ('D', 1)],
          'B': [('A', 1), ('C', 3), ('D', 3)],
          'C': [('A', 1), ('B', 3), ('D', 3)],
          'D': [('A', 1), ('B', 3), ('C', 3)]}

graph2 = {'A': [('B', 3), ('C', 4), ('E', 4)],
          'B': [('A', 3), ('D', 3), ('E', 1)],
          'C': [('A', 4), ('D', 2), ('E', 1), ('F', 3)],
          'D': [('B', 3), ('C', 2), ('E', 2), ('F', 1)],
          'E': [('A', 4), ('B', 1), ('C', 1), ('D', 2)],
          'F': [('C', 3), ('D', 1)],
          'G': [('B', 1), ('D', 2)]}

graph3 = {'A': [('P', 1), ('B', 4), ('C', 5), ('J', 1)],
          'B': [('O', 1), ('D', 4), ('C', 4), ('A', 4), ('P', 2)],
          'C': [('B', 4), ('I', 2), ('E', 3), ('F', 3), ('J', 3), ('A', 5)],
          'D': [('H', 3), ('K', 3), ('L', 4), ('E', 4), ('B', 4), ('O', 3)],
          'E': [('D', 4), ('L', 1), ('F', 4), ('C', 3)],
          'F': [('J', 4), ('C', 3), ('E', 4), ('M', 2)],
          'G': [('K', 3), ('N', 1), ('L', 3)],
          'H': [('K', 2), ('D', 3), ('O', 3)],
          'I': [('C', 2)],
          'J': [('A', 1), ('C', 3), ('F', 4)],
          'K': [('G', 3), ('D', 3), ('H', 2)],
          'L': [('D', 4), ('G', 3), ('M', 4), ('E', 1)],
          'M': [('L', 4), ('F', 2)],
          'N': [('G', 1)],
          'O': [('H', 3), ('D', 3), ('B', 1)],
          'P': [('B', 2), ('A', 1)]}

# print question3(graph3)

# QUESTION 5

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

def question5(ll, m):
    list_length = 0
    original_node = ll
    next_node = ll.next

    # Get list length
    while next_node:
        list_length += 1
        next_node = ll.next
        ll = ll.next

    ll = original_node
    target_node = None
    
    for i in range(list_length - m + 1):
        target_node = ll
        ll = ll.next

    return target_node.data

print question5(node1, 6)
        
