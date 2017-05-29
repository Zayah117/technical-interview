# QUESTION 1

def question1(s, t):
    # if t is larger than s return false
    if not t or not s or len(t) > len(s):
        return False

    # setup t_count to compare later
    t_count = {}
    for character in t:
        t_count[character] = t.count(character)

    print t_count

    # main loop
    for i in range(len(s) - len(t) + 1):
        
        s_count = {}
        for character in s[i:i+len(t)]:
            s_count[character] = s.count(character)

        if s_count == t_count:
            return True
        
    return False

print question1("udacity", "uda")
# True

print question1("udacity", "uuuuuuuuuudacity")
# False

print question1("udacity", None)
# False



# QUESTION 2

def is_palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

def question2(a):
    if not a:
        return None
    
    for num_of_letters in range(len(a)):
        for i in range(num_of_letters + 1):
            test_case = a[i:len(a)-num_of_letters+i]
            # print test_case
            if is_palindrome(test_case):
                return test_case
            
    return None

# print question2("racecarsarecool")
# racecar

# print question2("")
# None

# print question2(None)
# None



# QUESTION 3
def question3(G):
    # Get vertices from G
    try:
        vertices = sorted(G.keys())
    except AttributeError:
        return None

    # Setup dictionary S
    if vertices:
        S = {}
        S[vertices[0]] = []
    else:
        return None

    # Add vertices to S until it's as big as G
    while len(S) < len(G):
    	# this will be the new connection to add
        short_con = None

        # go through every vertex in S
        for vertex in S:
            # get the shortest edge from that vertex (that connects to G - S)
            new_con = get_short_edge(vertex, get_reverse_graph(G, S, vertices))

            # if it's not none
            if new_con[0] and new_con[1]:
            	# and if it's shorter than short_con
                if not short_con or short_con[1][1] > new_con[1][1]:
                	# new connection is now the shortest connection
                    short_vert = vertex
                    short_con = new_con
        
        # add shortest connection to S
        S[short_vert].append((short_con[0], short_con[1][1]))
        S[short_con[0]] = [short_con[1]]

    return S

def get_short_edge(comp_vertex, G):
    short_edge = None
    short_vertex = None
    for vertex in G:
        for connected_edge in G[vertex]:
            # if connection_edge is connected to comp_vertex
            if connected_edge[0] == comp_vertex:
                # make edge short edge if it is shorter than previous short edge
                if not short_edge or short_edge[1] > connected_edge[1]:
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

# print question3(graph1)
# {'A': [('C', 1), ('B', 1), ('D', 1)], 'C': [('A', 1)], 'B': [('A', 1)], 'D': [('A', 1)]}

# print question3({})
# None

# print question3(None)
# None

# QUESTION 4

def question4(T, r, n1, n2):
    n1_ancestors = get_ancestors(T, n1, r, [])
    n2_ancestors = get_ancestors(T, n2, r, [])

    if n1 not in n1_ancestors or n2 not in n2_ancestors:
        return None

    if len(n1_ancestors) < len(n2_ancestors):
        short_list = n1_ancestors
    else:
        short_list = n2_ancestors

    least_common_ancestor = None
    for i in range(len(short_list)):
        if n1_ancestors[i] == n2_ancestors[i]:
            least_common_ancestor = short_list[i]

    return least_common_ancestor

def get_ancestors(T, n, r, ancestors, level=0):
    ancestors.append(r)
    level += 1

    try:
        for i in range(len(T[r])):
            if ((n > r and i > r) or (n < r and i < r)) and T[r][i] == 1:
                return get_ancestors(T, n, i, ancestors, level)
    except IndexError:
        return []

    return ancestors

tree1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# print question4(tree1, 7, 9, 14)
# 11

# print question4(tree1, 7, -24, 100)
# None

# print question4([], 7, 0, 0)
# None

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

    if target_node:
        return target_node.data
    else:
        return None

# print question5(node1, 4)
# 4

# print question5(node7, 4)
# None

# print question5(node1, 100)
# None
        
