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

# print question1("udacity", "uda")
# True

# print question1("udacity", "uuuuuuuuuudacity")
# False

# print question1("udacity", None)
# False



# QUESTION 2

def question2(a):
    if not a:
        return
    N = len(a)
    N = 2*N+1 # Position count

    # Setup L
    L = [0] * N
    L[0] = 0
    L[1] = 1

    C = 1 # centerPosition
    R = 2 # centerRightPosition
    i = 0 # currentRightPosition
    iMirror = 0 # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1

    for i in xrange(2,N):
        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i

        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)

        # Expand palindrom centered at i. If even increase LPS by 1. If odd compare characters and increase.
        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or \
                    (a[(i + L[i] + 1) / 2] == a[(i - L[i] - 1) / 2])):
                L[i]+=1
        except Exception as e:
            pass

        # Update maxLPSLength
        if L[i] > maxLPSLength:
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        # Adjust center position based on expanded palindrome
        if i + L[i] > R:
            C = i
            R = i + L[i]

    start = (maxLPSCenterPosition - maxLPSLength) / 2
    end = start + maxLPSLength - 1

    return a[start:end+1]

# print question2("racecarsarecool")
# racecar

# print question2("")
# None

# print question2(None)
# None



# QUESTION 3
def question3(G):
    # Get structured edge list
    edges = structured_edge_list(G)

    S = []
    for edge in sorted_edges(edges):
        test = S[:]
        test.append(edge)
        if not is_cyclic(G, test):
            S.append(edge)
    return S

def is_cyclic(G, edges):
    # Initialize parent array
    parent_dict = {}
    for vertex in G:
        parent_dict[vertex] = -1

    # Main loop
    for edge in edges:
        src_parent = find_parent(edge['src'], parent_dict)
        dest_parent = find_parent(edge['dest'], parent_dict)

        # If cycle is found
        if src_parent == dest_parent:
            return True
        # Otherwise, union
        else:
            parent_dict[src_parent] = dest_parent

def find_parent(v, parent_dict):
    if parent_dict[v] == -1:
        return v
    else:
        return find_parent(parent_dict[v], parent_dict)

def structured_edge_list(G):
    edge_list = []
    for vertex in G:
        for edge in G[vertex]:
            new_element = {}
            new_element['weight'] = edge[1]
            new_element['src'] = vertex
            new_element['dest'] = edge[0]

            # Don't add duplicates
            if not {'weight': new_element['weight'],
                    'src': new_element['dest'],
                    'dest': new_element['src']} in edge_list:
                edge_list.append(new_element)

    # edge_list = sorted(edge_list, key=lambda d: d['weight'])

    return edge_list

def sorted_edges(structured_list):
    return sorted(structured_list, key=lambda d: d['weight'])
    pass
        

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

print question3(graph2)
# print question3({'A': [('C', 1), ('B', 1), ('D', 1)], 'C': [('A', 1)], 'B': [('A', 1)], 'D': [('A', 1)]})

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
        
